import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from shop.models import Shop

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    permissions = models.ManyToManyField('Permission', related_name='roles')
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="roles",    
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["shop", "name"], name="unique_role_name_per_shop"),
        ]

    def __str__(self):
        return self.name

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.ForeignKey('Role', on_delete=models.PROTECT, related_name='users',null=True, blank=True)

    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='users',null=True, blank=True)
    branch = models.ForeignKey('shop.Branch', on_delete=models.PROTECT, related_name='users',null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_permissions(self):
        if not self.role:
            return set()
        return set(
            self.role.permissions.values_list("code", flat=True)
        )        
    def has_perm(self, perm, obj=None):
        """
        Called by Django and DRF internally.
        `perm` is expected to be a permission code string, e.g. "sale:create".
        Platform superusers bypass all checks.
        """
        if not self.is_active:
            return False
        if self.is_superuser:
            return True
        return perm in self.get_permissions()
 
    def has_module_perms(self, app_label):
        """Required by Django admin."""
        return self.is_superuser
    
    def clean(self):
        super().clean()
        # Ensure branch requires shop
        if self.branch and not self.shop:
            raise ValidationError("Branch requires a shop.")

        if self.role and self.shop and self.role.shop_id != self.shop_id:
            raise ValidationError({"role": "Assigned role must belong to the same shop as the user."})

    def save(self, *args, **kwargs):
        if self.branch:
            self.shop = self.branch.shop
        self.full_clean()

        super().save(*args, **kwargs)


    def __str__(self):
        return self.email
    
