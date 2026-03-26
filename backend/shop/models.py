import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Shop(models.Model):
    """
    Top-level tenant. Every piece of business data is scoped to a Shop.
 
    `owner` is the ADMIN user. We use SET_NULL so the shop isn't destroyed
    if the owner account is deleted — the platform admin can reassign.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_shops",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name
 
 
class Branch(models.Model):
    """
    A physical location belonging to a Shop.
    `manager` is a User with role=MANAGER scoped to this branch.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="branches",
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    manager = models.OneToOneField(      
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_branch",  
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
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
    sku = models.CharField(max_length=100)        # Stock Keeping Unit(product code)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
 
    # Alert threshold: when branch stock falls below this, trigger low-stock alert
    reorder_threshold = models.PositiveIntegerField(default=10)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        # SKU must be unique within a shop
        unique_together = [("shop", "sku")]
 
    def __str__(self):
        return f"{self.name} ({self.sku})"
