from django.contrib import admin
from .models import Customer, Guest, Product, Collection, Diamond, Employee, StaffManagement,Order,OrderProduct, Cart, Warranty, Certification, Promotion,ProductPromotion,DiamondPricing,SettingPrice,SalesReport,SupportTicket,Feedback
# Register your models here.
admin.site.register(Customer)
admin.site.register(Guest)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Employee)
admin.site.register(StaffManagement)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Cart)
admin.site.register(Warranty)
admin.site.register(Certification)
admin.site.register(Promotion)
admin.site.register(ProductPromotion)
admin.site.register(DiamondPricing)
admin.site.register(SettingPrice)
admin.site.register(SalesReport)
admin.site.register(SupportTicket)
admin.site.register(Feedback)

class DiamondAdmin(admin.ModelAdmin): 
    list_display = ("origin", "carat_weight", "color", "clarity", "cut", "price")

admin.site.register(Diamond, DiamondAdmin)