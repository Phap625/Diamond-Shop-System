from django.contrib import admin
from .models import Customer, Diamond, Order, OrderDetail

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Email', 'Phone', 'CreatedAt')
    search_fields = ('FullName', 'Email', 'Phone')
    list_filter = ('CreatedAt',)

@admin.register(Diamond)
class DiamondAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Carat', 'Price', 'Stock', 'Certificate', 'CreatedAt')
    search_fields = ('Name', 'Certificate')
    list_filter = ('Carat', 'Price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'OrderDate', 'TotalPrice', 'Status')
    list_filter = ('Status', 'OrderDate')
    search_fields = ('Customer__FullName',)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('Order', 'Diamond', 'Quantity', 'Price')
    search_fields = ('Order__id', 'Diamond__Name')
