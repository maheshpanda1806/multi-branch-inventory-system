from rest_framework import serializers

from .models import Branch, Product, Shop


class ShopSerializer(serializers.ModelSerializer):
    owner_id = serializers.SerializerMethodField()
    owner_email = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "owner_id",
            "owner_email",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "owner_id", "owner_email"]

    def get_owner_id(self, obj):
        """Get the owner's user ID"""
        owner = obj.owner
        return str(owner.id) if owner else None

    def get_owner_email(self, obj):
        """Get the owner's email"""
        owner = obj.owner
        return owner.email if owner else None


class BranchSerializer(serializers.ModelSerializer):
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
    )
    manager_id = serializers.SerializerMethodField()
    manager_email = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = [
            "id",
            "name",
            "address",
            "shop",
            "shop_id",
            "manager_id",
            "manager_email",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "shop", "manager_id", "manager_email"]

    def get_manager_id(self, obj):
        """Get the manager's user ID"""
        manager = obj.manager
        return str(manager.id) if manager else None

    def get_manager_email(self, obj):
        """Get the manager's email"""
        manager = obj.manager
        return manager.email if manager else None

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
