from django.db import models

from shop.models import Product, Branch

# Create your models here.
class Inventory(models.Model):
    """
    Tracks stock of a Product at a specific Branch.
    One row per (branch, product) pair.
 
    reserved_quantity: stock set aside for approved-but-not-dispatched orders.
    available_quantity = quantity - reserved_quantity  (computed property)
    """
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="inventory",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="inventory",
    )
    quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        unique_together = [("branch", "product")]  # one row per branch-product
 
    @property
    def available_quantity(self):
        return self.quantity - self.reserved_quantity
 
    @property
    def is_low_stock(self):
        return self.quantity <= self.product.reorder_threshold
 
    def __str__(self):
        return f"{self.product.name} @ {self.branch.name}: {self.quantity}"
