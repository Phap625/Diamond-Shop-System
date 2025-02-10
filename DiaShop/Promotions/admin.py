from django.contrib import admin
from .models import OrderDetail

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('OrderDetailID', 'OrderID', 'DiamondID', 'Quantity', 'UnitPrice', 'FreeItems')
    search_fields = ('OrderID__id', 'DiamondID__id')
    list_filter = ('Quantity',)
    ordering = ('-Quantity',)
