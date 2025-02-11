from django.contrib import admin
from .models import Question,Choice
admin.site.register(Question)
admin.site.register(Choice)

from .models import Diamond
admin.site.register(Diamond)

class DiamondAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Carat', 'Price', 'Stock', 'Certificate', 'CreatedAt')
    search_fields = ('Name', 'Certificate')

from .models import Customer
admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Email', 'Phone', 'CreatedAt')
    search_fields = ('FullName', 'Email', 'Phone')

from .models import Order
admin.site.register(Order)

class OrderAmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'OrderDate', 'TotalPrice', 'Status')
    search_fields = ('Customer__FullName', 'Status')


from .models import OrderDetail
admin.site.register(OrderDetail)

class OrderAmin(admin.ModelAdmin):
    list_display = ('id', 'Order', 'Diamond', 'Quantity', 'Price')
    search_fields = ('Order__id', 'Diamond__Name')

from .models import Supplier
admin.site.register(Supplier)
class OrderAmin(admin.ModelAdmin):
    list_display = ('Name', 'ContactPerson', 'Phone', 'Email', 'Address')
    search_fields = ('Name', 'ContactPerson')


from .models import Inventory
admin.site.register(Inventory)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('Diamond', 'Supplier', 'Quantity', 'PurchasePrice', 'PurchaseDate')
    search_fields = ('Diamond__Name', 'Supplier__Name')

from.models import Employee
admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Email', 'Phone', 'Position', 'Salary', 'HireDate')
    search_fields = ('FullName', 'Email', 'Phone')

from.models import Transaction
admin.site.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Order', 'PaymentMethod', 'Amount', 'TransactionDate')
    search_fields = ('Order__id', 'PaymentMethod')
    list_filter = ('PaymentMethod', 'TransactionDate')
