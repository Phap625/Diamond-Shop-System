from django.contrib import admin
from .models import Diamond

@admin.register(Diamond)
class DiamondAdmin(admin.ModelAdmin):
    list_display = ('DiamondID', 'Name', 'Carat', 'Cut', 'Color', 'Clarity', 'Price', 'Stock', 'CreatedAt')
    search_fields = ('Name', 'Cut', 'Color', 'Clarity')
    list_filter = ('Cut', 'Color', 'Clarity', 'CreatedAt')
    ordering = ('-CreatedAt',)
