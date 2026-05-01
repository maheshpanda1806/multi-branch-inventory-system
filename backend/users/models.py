import uuid
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

class Permission(models.Model):
    """
    Platform-wide permission definitions.
    Reusable across any shop or role.

    UNCHANGED.
    Examples: "shop:own", "branch:manage", "sale:create"
    """
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    Shop-scoped role with a set of permissions.

    CHANGED: Added `is_branch_scoped` flag.
    - is_branch_scoped=False → shop-level role (Admin/Owner), no branch required
    - is_branch_scoped=True  → branch-level role (Manager, Cashier), branch required
    This flag is enforced in ShopMembership.clean().
    """
    name = models.CharField(max_length=255)
    shop = models.ForeignKey(
        'shop.Shop',
        on_delete=models.CASCADE,
        related_name="roles",
    )
    permissions = models.ManyToManyField(
        'Permission',
        related_name='roles',
        blank=True
    )
    # NEW: distinguishes shop-level vs branch-level roles
    is_branch_scoped = models.BooleanField(
        default=False,
        help_text=(
            "If True, users with this role must be assigned to a branch. "
            "e.g. Manager, Cashier. "
            "If False, role applies at shop level. e.g. Admin/Owner."
        )
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["shop", "name"],
                name="unique_role_name_per_shop"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.shop.name})"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Platform-level identity only. Holds NO shop/branch/role context.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)       # platform admin only
    is_superuser = models.BooleanField(default=False)   # platform admin only

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def get_memberships(self, shop_id=None):
        queryset = self.memberships.select_related("role").filter(is_active=True)
        if shop_id is not None:
            queryset = queryset.filter(shop_id=shop_id)
        return queryset

    def get_membership(self, shop_id):
        return self.get_memberships(shop_id).first()

    def get_permissions_for_shop(self, shop_id):
        """
        Returns a set of permission codes for this user within a specific shop.
        """
        return set(
            Permission.objects.filter(
                roles__memberships__user=self,
                roles__memberships__shop_id=shop_id,
                roles__memberships__is_active=True,
                is_active=True,
            ).values_list("code", flat=True).distinct()
        )

    def has_perm(self, perm, obj=None):
        """
        CHANGED: `obj` is now expected to be a shop_id (UUID/int).
        Pass shop_id from your DRF permission class via request.shop_id.

        Platform superusers bypass all checks.
        """
        if not self.is_active:
            return False
        if self.is_superuser:
            return True
        if obj is not None:
            return perm in self.get_permissions_for_shop(obj)
        return False

    def has_module_perms(self, app_label):
        """Required by Django admin. Platform superusers only."""
        return self.is_superuser

    def __str__(self):
        return self.email


class ShopMembership(models.Model):
    """
    The single source of truth for user access control.

    Ties a User to a Shop with one Role and an optional Branch.
    Replaces the old User.shop / User.branch / User.role FK approach.

    Rules enforced in clean():
    - One membership per user per shop/role/branch combination
    - Role must belong to the same shop
    - Branch must belong to the same shop
    - Branch-scoped roles require a branch
    - Shop-level roles must NOT have a branch assigned
    - Only ONE owner (shop:own role) allowed per shop
    - Only ONE manager (branch:manage role) allowed per branch
    - Extra memberships in other shops require shop:own on every membership

    Note: One user CAN have multiple roles in the same shop/branch
    (e.g., both Manager + Supervisor), but cannot hold shop:own or branch:manage twice.

    branch=None → shop-level role  (Admin/Owner)
    branch=set  → branch-level role (Manager, Cashier, etc.)
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    shop = models.ForeignKey(
        'shop.Shop',
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="memberships"
    )
    branch = models.ForeignKey(
        'shop.Branch',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="memberships"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "shop", "role"],
                condition=Q(branch__isnull=True),
                name="unique_shop_level_membership_per_user_role",
            ),
            models.UniqueConstraint(
                fields=["user", "shop", "role", "branch"],
                condition=Q(branch__isnull=False),
                name="unique_branch_membership_per_user_role_branch",
            )
        ]

    def clean(self):
        # 1. Role must belong to the same shop as this membership
        if self.role and self.shop and self.role.shop_id != self.shop_id:
            raise ValidationError("Role must belong to the same shop.")

        # 2. Branch must belong to the same shop as this membership
        if self.branch and self.shop and self.branch.shop_id != self.shop_id:
            raise ValidationError("Branch must belong to the same shop.")

        # 3. Branch-scoped roles must have a branch assigned
        if self.role and self.role.is_branch_scoped and not self.branch:
            raise ValidationError(
                f"Role '{self.role.name}' requires a branch assignment."
            )

        # 4. Shop-level roles must NOT have a branch assigned
        if self.role and not self.role.is_branch_scoped and self.branch:
            raise ValidationError(
                f"Role '{self.role.name}' is a shop-level role and cannot be assigned to a branch."
            )

        # 5. Only one owner per shop (only one role with 'shop:own' permission)
        if self.shop and self.role and self.is_active:
            is_owner_role = self.role.permissions.filter(
                code="shop:own",
                is_active=True
            ).exists()
            
            if is_owner_role:
                # Check if another active membership with shop:own already exists in this shop
                existing_owner = ShopMembership.objects.filter(
                    shop=self.shop,
                    role__permissions__code="shop:own",
                    role__permissions__is_active=True,
                    is_active=True
                ).exclude(pk=self.pk).exists()
                
                if existing_owner:
                    raise ValidationError(
                        "Only one owner is allowed per shop."
                    )

        # 6. Only one manager per branch (only one role with 'branch:manage' permission)
        if self.branch and self.role and self.is_active:
            is_manager_role = self.role.permissions.filter(
                code="branch:manage",
                is_active=True
            ).exists()
            
            if is_manager_role:
                # Check if another active membership with branch:manage already exists in this branch
                existing_manager = ShopMembership.objects.filter(
                    branch=self.branch,
                    role__permissions__code="branch:manage",
                    role__permissions__is_active=True,
                    is_active=True
                ).exclude(pk=self.pk).exists()
                
                if existing_manager:
                    raise ValidationError(
                        "Only one manager is allowed per branch."
                    )

        # 7. Multi-shop rule:
        #    Only users whose existing memberships all carry 'shop:own'
        #    can be added to another shop.
        existing = ShopMembership.objects.filter(
            user=self.user
        ).exclude(pk=self.pk)

        if self.shop and existing.exclude(shop_id=self.shop_id).exists():
            # All existing memberships must be admin-level (every one must have shop:own)
            non_owner_count = existing.exclude(
                role__permissions__code="shop:own",
                role__permissions__is_active=True
            ).count()

            if non_owner_count > 0:
                raise ValidationError(
                    "Non-admin users can only belong to one shop."
                )

            # The new role being added must also be admin-level
            is_new_role_admin = self.role.permissions.filter(
                code="shop:own",
                is_active=True
            ).exists()

            if not is_new_role_admin:
                raise ValidationError(
                    "Only shop owners can have memberships across multiple shops."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} @ {self.shop.name} ({self.role.name})"

# 1 user → multiple memberships	✅ YES
# 1 user → multiple roles in same shop	✅ YES
# 1 user → multiple roles in same branch	✅ YES
# Only 1 owner per shop	✅ ENFORCED
# Only 1 manager per branch	✅ ENFORCED
# 1 user → memberships across different shops	✅ YES (with rules) (ONLY FOR ADMINS)