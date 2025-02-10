from django.db import models

class Inventory(models.Model):
    InventoryID = models.AutoField(primary_key=True)
    SupplierID = models.ForeignKey('Supplier', on_delete=models.CASCADE)  # Đảm bảo có model Supplier
    DiamondID = models.ForeignKey('Diamond', on_delete=models.CASCADE)  # Đảm bảo có model Diamond
    Quantity = models.IntegerField()
    PurchasePrice = models.DecimalField(max_digits=15, decimal_places=2)
    PurchaseDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory {self.InventoryID} - Supplier {self.SupplierID} - Diamond {self.DiamondID}"
