from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('TransactionID', 'OrderID', 'PaymentMethod', 'Amount', 'TransactionDate')
    search_fields = ('TransactionID', 'OrderID__id', 'PaymentMethod')
    list_filter = ('PaymentMethod', 'TransactionDate')
    ordering = ('-TransactionDate',)
