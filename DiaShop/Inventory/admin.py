from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('InventoryID', 'SupplierID', 'DiamondID', 'Quantity', 'PurchasePrice', 'PurchaseDate')
    search_fields = ('SupplierID__id', 'DiamondID__id')
    list_filter = ('PurchaseDate',)
    ordering = ('-PurchaseDate',)
