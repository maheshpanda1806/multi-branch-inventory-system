from django.contrib import admin
from .models import User, Permission, Role, ShopMembership


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'created_at')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
    ordering = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'is_branch_scoped', 'is_active', 'created_at')
    list_filter = ('shop', 'is_branch_scoped', 'is_active')
    search_fields = ('name', 'shop__name')
    filter_horizontal = ('permissions',)
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(ShopMembership)
class ShopMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop', 'role', 'branch', 'is_active', 'created_at')
    list_filter = ('shop', 'role', 'is_active', 'role__is_branch_scoped')
    search_fields = ('user__email', 'user__username', 'shop__name', 'branch__name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    def get_readonly_fields(self, request, obj=None):
        """Make user and shop read-only on edit to prevent data inconsistency"""
        if obj is not None:  # editing an existing object
            return self.readonly_fields + ('user', 'shop')
        return self.readonly_fields