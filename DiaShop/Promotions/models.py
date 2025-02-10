from django.db import models

class OrderDetail(models.Model):
    OrderDetailID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)  # Đảm bảo có model Order
    DiamondID = models.ForeignKey('Diamond', on_delete=models.CASCADE)  # Đảm bảo có model Diamond
    Quantity = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=15, decimal_places=2)
    FreeItems = models.IntegerField(default=0)  # Mua 10 tặng 1

    def save(self, *args, **kwargs):
        # Áp dụng khuyến mãi: Mua 10 tặng 1
        if self.Quantity >= 10:
            self.FreeItems = self.Quantity // 10
        else:
            self.FreeItems = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.OrderID} - Diamond {self.DiamondID} - Quantity {self.Quantity}"
