from django.contrib import admin
from .models import Shop,Branch,Product
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)

    list_filter = ('owner',)
    search_fields = ('name', 'owner')
    ordering = ('id',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop','name', 'manager',)

    list_filter = ('manager','shop')
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','shop','name','sku','unit_price') 
    list_filter = ('shop',)
    search_fields = ('name','sku','name',)
    ordering = ('id',)
