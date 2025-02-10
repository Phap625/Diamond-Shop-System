from django.db import models

class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    TransactionID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)  # Đảm bảo có model Order
    PaymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    Amount = models.DecimalField(max_digits=15, decimal_places=2)
    TransactionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.TransactionID} - {self.PaymentMethod}"
