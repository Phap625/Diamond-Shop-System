import uuid
from django.contrib.auth.models import User
from django.db import models
from Products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        status = "Hoàn thành" if self.complete else "Chưa hoàn thành"
        return f"{self.customer} đặt hàng - Trạng thái: {status}"

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShoppingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
