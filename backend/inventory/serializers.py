from rest_framework import serializers

from .models import Inventory
from shop.models import Branch, Product


class InventorySerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        source="branch",
        queryset=Branch.objects.all(),
    )
    product_id = serializers.PrimaryKeyRelatedField(
        source="product",
        queryset=Product.objects.all(),
    )
    available_quantity = serializers.IntegerField(read_only=True)
    is_low_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Inventory
        fields = [
            "id",
            "branch",
            "branch_id",
            "product",
            "product_id",
            "quantity",
            "reserved_quantity",
            "available_quantity",
            "is_low_stock",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "branch",
            "product",
            "available_quantity",
            "is_low_stock",
            "updated_at",
        ]
