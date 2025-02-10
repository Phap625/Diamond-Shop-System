from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Email', 'Phone', 'CreatedAt')
    search_fields = ('FullName', 'Email', 'Phone')
    list_filter = ('CreatedAt',)
