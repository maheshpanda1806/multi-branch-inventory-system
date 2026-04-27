from django.contrib import admin
from .models import Shop, Branch, Product


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_owner', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')

    def get_owner(self, obj):
        """Display the shop owner derived from ShopMembership"""
        owner = obj.owner
        return owner.email if owner else "No owner"
    get_owner.short_description = "Owner"


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'name', 'get_manager', 'created_at')
    list_filter = ('shop',)
    search_fields = ('name', 'shop__name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')

    def get_manager(self, obj):
        """Display the branch manager derived from ShopMembership"""
        manager = obj.manager
        return manager.email if manager else "No manager"
    get_manager.short_description = "Manager"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'name', 'sku', 'unit_price', 'created_at')
    list_filter = ('shop', 'category')
    search_fields = ('name', 'sku', 'category')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
