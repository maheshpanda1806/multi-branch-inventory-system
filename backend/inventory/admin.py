from django.contrib import admin
from .models import Inventory
# Register your models here.

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('branch','product','quantity','reserved_quantity',)

    list_filter = ('branch',)
    search_fields = ('product',)
    ordering = ('branch',)