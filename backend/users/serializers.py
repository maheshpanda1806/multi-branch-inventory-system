from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from .models import Permission, Role, User
from shop.models import Branch, Shop

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "code",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        source="permissions",
        write_only=True,
        required=False,
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
    )

    class Meta:
        model = Role
        fields = [
            "id",
            "name",
            "shop",
            "shop_id",
            "permissions",
            "permission_ids",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "shop", "permissions"]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, style={"input_type": "password"})
    role_id = serializers.PrimaryKeyRelatedField(
        source="role",
        queryset=Role.objects.all(),
        allow_null=True,
        required=False,
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
        allow_null=True,
        required=False,
    )
    branch_id = serializers.PrimaryKeyRelatedField(
        source="branch",
        queryset=Branch.objects.all(),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "role",
            "role_id",
            "shop",
            "shop_id",
            "branch",
            "branch_id",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "role",
            "shop",
            "branch",
            "is_staff",
            "is_superuser",
        ]

    def validate(self, attrs):
        instance = getattr(self, "instance", None)
        password = attrs.get("password")
        role = attrs.get("role", getattr(instance, "role", None))
        branch = attrs.get("branch", getattr(instance, "branch", None))
        shop = attrs.get("shop", getattr(instance, "shop", None))

        if instance is None and not password:
            raise serializers.ValidationError(
                {"password": "Password is required when creating a user."}
            )

        if password:
            candidate_data = {
                "username": attrs.get("username", getattr(instance, "username", "")),
                "email": attrs.get("email", getattr(instance, "email", "")),
            }
            candidate_user = instance or User(**candidate_data)

            try:
                validate_password(password=password, user=candidate_user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError({"password": list(exc.messages)})

        if branch is not None:
            branch_shop = branch.shop
            if shop is not None and shop != branch_shop:
                raise serializers.ValidationError(
                    {"shop_id": "shop_id must match the selected branch."}
                )
            shop = branch_shop

        if role is not None:
            if shop is not None and role.shop != shop:
                raise serializers.ValidationError(
                    {"role_id": "role_id must belong to the same shop as the user."}
                )
            if shop is None:
                shop = role.shop

        attrs["shop"] = shop
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        return User.objects.create_user(password=password, **validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)

        instance.save()
        return instance