from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True)
    TotalPrice = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.Customer.FullName}"

class OrderDetail(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Diamond = models.ForeignKey(Diamond, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=False)
    Price = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    def __str__(self):
        return f"Order {self.Order.id} - {self.Diamond.Name}"
