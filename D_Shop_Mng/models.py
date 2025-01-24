from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.
def current_datetime():
    return timezone.now()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    def __str__(self): 
        return self.name

class Guest(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self): 
        return f"Guest {self.session_id}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self): 
        return self.name
    
class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='collections')

    def __str__(self): 
        return self.name

class Diamond(models.Model):
    origin = models.CharField(max_length=255)
    carat_weight = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)
    clarity = models.CharField(max_length=50)
    cut = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.carat_weight} carat {self.color} {self.clarity} {self.cut}"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StaffManagement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f"{self.task} for {self.employee.name}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, blank=True, null=True)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    ring_size = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending')

    def __str__(self): 
        return f"Order {self.id} by {self.customer or self.guest}"
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): 
        return f"{self.quantity} of {self.product.name} in {self.order}"
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self): 
        return f"{self.customer.name}'s cart"
    
class Warranty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warranty_period = models.IntegerField()
    warranty_details = models.TextField()

    def __str__(self): 
        return f"Warranty for {self.product.name}"
    
class Certification(models.Model):
    diamond = models.ForeignKey(Diamond, on_delete=models.CASCADE)
    certification_details = models.TextField()
    certification_date = models.DateField()

    def __str__(self): 
        return f"Certification for {self.diamond}"
    
class Promotion(models.Model):
    promotion_name = models.CharField(max_length=255)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self): 
        return self.promotion_name

class ProductPromotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} under {self.promotion.promotion_name}"
    
class DiamondPricing(models.Model):
    diamond_origin = models.CharField(max_length=255)
    carat_weight = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)
    clarity = models.CharField(max_length=50)
    cut = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pricing for {self.carat_weight} carat {self.color} {self.clarity} {self.cut}"
    
class SettingPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    markup_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self): 
        return f"Price setting for {self.product.name}"
    
class SalesReport(models.Model):
    report_date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    best_selling_products = models.TextField()

    def __str__(self):
        return f"Sales Report for {self.report_date}"
    
class SupportTicket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    issue = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Ticket {self.id} by {self.customer.name}"
    
class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"Feedback {self.id} by {self.customer.name}"

