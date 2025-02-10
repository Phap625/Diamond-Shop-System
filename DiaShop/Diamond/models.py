from django.db import models

class Diamond(models.Model):
    DiamondID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Carat = models.FloatField()
    Cut = models.CharField(max_length=50)
    Color = models.CharField(max_length=1)
    Clarity = models.CharField(max_length=10)
    Price = models.DecimalField(max_digits=15, decimal_places=2)
    Stock = models.IntegerField()
    Certificate = models.CharField(max_length=255, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    ImageURL = models.URLField(max_length=500, blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
