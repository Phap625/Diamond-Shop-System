from django.db import models
from accounts.models import Customer
from Diamond.models import Diamond


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    OrderDate = models.DateTimeField(auto_now_add=True)
    TotalPrice = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.Customer.FullName}"

class OrderDetail(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_details")
    Diamond = models.ForeignKey(Diamond, on_delete=models.CASCADE, related_name="diamond_orders")
    Quantity = models.IntegerField(null=False)
    Price = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    def __str__(self):
        return f"Order {self.Order.id} - {self.Diamond.Name}"
