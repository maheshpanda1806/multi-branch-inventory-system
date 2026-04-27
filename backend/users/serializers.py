from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from .models import Permission, Role, User, ShopMembership
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
            "is_branch_scoped",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "shop", "permissions"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "is_staff",
            "is_superuser",
        ]

    def validate(self, attrs):
        instance = getattr(self, "instance", None)
        password = attrs.get("password")

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


class ShopMembershipSerializer(serializers.ModelSerializer):
    """
    Serializer for ShopMembership - the single source of truth for user access control.
    Handles user-shop-role-branch relationships with proper validation.
    """
    user_id = serializers.PrimaryKeyRelatedField(
        source="user",
        queryset=User.objects.all(),
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        source="shop",
        queryset=Shop.objects.all(),
    )
    role_id = serializers.PrimaryKeyRelatedField(
        source="role",
        queryset=Role.objects.all(),
    )
    branch_id = serializers.PrimaryKeyRelatedField(
        source="branch",
        queryset=Branch.objects.all(),
        allow_null=True,
        required=False,
    )
    
    # Read-only nested serializers for display
    user_email = serializers.CharField(source="user.email", read_only=True)
    shop_name = serializers.CharField(source="shop.name", read_only=True)
    role_name = serializers.CharField(source="role.name", read_only=True)
    branch_name = serializers.CharField(source="branch.name", read_only=True, allow_null=True)
    is_branch_scoped = serializers.BooleanField(source="role.is_branch_scoped", read_only=True)

    class Meta:
        model = ShopMembership
        fields = [
            "id",
            "user",
            "user_id",
            "user_email",
            "shop",
            "shop_id",
            "shop_name",
            "role",
            "role_id",
            "role_name",
            "is_branch_scoped",
            "branch",
            "branch_id",
            "branch_name",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "user",
            "shop",
            "role",
            "branch",
            "user_email",
            "shop_name",
            "role_name",
            "branch_name",
            "is_branch_scoped",
        ]

    def validate(self, attrs):
        """Validate membership data before saving"""
        instance = getattr(self, "instance", None)
        
        user = attrs.get("user", getattr(instance, "user", None))
        shop = attrs.get("shop", getattr(instance, "shop", None))
        role = attrs.get("role", getattr(instance, "role", None))
        branch = attrs.get("branch", getattr(instance, "branch", None))

        # Validate role belongs to shop
        if role and shop and role.shop_id != shop.id:
            raise serializers.ValidationError(
                {"role_id": "Role must belong to the same shop."}
            )

        # Validate branch belongs to shop
        if branch and shop and branch.shop_id != shop.id:
            raise serializers.ValidationError(
                {"branch_id": "Branch must belong to the same shop."}
            )

        # Validate branch-scoped roles have a branch
        if role and role.is_branch_scoped and not branch:
            raise serializers.ValidationError(
                {"branch_id": f"Role '{role.name}' requires a branch assignment."}
            )

        # Validate shop-level roles don't have a branch
        if role and not role.is_branch_scoped and branch:
            raise serializers.ValidationError(
                {"branch_id": f"Role '{role.name}' is a shop-level role and cannot be assigned to a branch."}
            )

        return attrs

    def create(self, validated_data):
        """Create a new ShopMembership with full validation"""
        membership = ShopMembership(**validated_data)
        membership.full_clean()
        membership.save()
        return membership

    def update(self, instance, validated_data):
        """Update ShopMembership with full validation"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.full_clean()
        instance.save()
        return instance