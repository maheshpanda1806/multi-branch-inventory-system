from rest_framework import serializers

from .models import Branch, Product, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class BranchSerializer(serializers.ModelSerializer):
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
    )
    class Meta:
        model = Branch
        fields = [
            "id",
            "name",
            "address",
            "shop",
            "shop_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "shop"]

    def validate(self, attrs):
        instance = getattr(self, "instance", None)
        shop = attrs.get("shop", getattr(instance, "shop", None))

        return attrs


class ProductSerializer(serializers.ModelSerializer):
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "sku",
            "category",
            "description",
            "unit_price",
            "reorder_threshold",
            "shop",
            "shop_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "shop"]
