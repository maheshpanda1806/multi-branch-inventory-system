import uuid
from django.db import models
from django.conf import settings

class Shop(models.Model):
    """
    Top-level tenant. Every piece of business data is scoped to a Shop.
    owner is a @property derived from ShopMembership
    so there's no FK drift between the role system and ownership.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def owner(self):
        """
        Returns the user in this shop whose role carries 'shop:own' permission.
        No FK needed — derived from the membership/role system.
        """
        from users.models import ShopMembership
        membership = (
            ShopMembership.objects
            .select_related("user")
            .filter(
                shop=self,
                role__permissions__code="shop:own",
                role__permissions__is_active=True,
                is_active=True
            )
            .first()
        )
        return membership.user if membership else None

    def __str__(self):
        return self.name


class Branch(models.Model):
    """
    A physical location belonging to a Shop.
    manager is a @property derived from ShopMembership
    so there's no FK drift between the role system and management.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="branches",
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def manager(self):
        """
        Returns the user assigned to this branch whose role carries
        'branch:manage' permission.
        No FK needed — derived from the membership/role system.
        """
        from users.models import ShopMembership
        membership = (
            ShopMembership.objects
            .select_related("user")
            .filter(
                branch=self,
                role__permissions__code="branch:manage",
                role__permissions__is_active=True,
                is_active=True
            )
            .first()
        )
        return membership.user if membership else None

    def __str__(self):
        return f"{self.shop.name} — {self.name}"


class Product(models.Model):
    """
    Products are defined at the Shop level (not per-branch).
    Stock at each branch is tracked separately via Inventory.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_threshold = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("shop", "sku")]

    def __str__(self):
        return f"{self.name} ({self.sku})"