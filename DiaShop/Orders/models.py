from django.db import models

class Customer(models.Model):
    FullName = models.CharField(max_length=255, null=False)
    Email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    Phone = models.CharField(max_length=20, unique=True, null=False)
    Address = models.TextField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FullName

class Diamond(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Carat = models.FloatField(null=False)
    Price = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    Stock = models.IntegerField(null=False)
    Certificate = models.CharField(max_length=255, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    ImageURL = models.URLField(max_length=500, blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

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
