from django.contrib import admin
from .models import Customer, Diamond, Order, OrderDetail
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'OrderDate', 'TotalPrice', 'Status')
    list_filter = ('Status', 'OrderDate')
    search_fields = ('Customer__FullName',)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('Order', 'Diamond', 'Quantity', 'Price')
    search_fields = ('Order__id', 'Diamond__Name')
