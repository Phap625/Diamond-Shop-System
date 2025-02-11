from django.db import models

class Diamond(models.Model):
    diamond_id = models.AutoField(primary_key=True, verbose_name="Diamond ID")
    name = models.CharField(max_length=255, verbose_name="Name", help_text="Name of the diamond")
    carat = models.FloatField(verbose_name="Carat", help_text="Carat weight of the diamond")
    cut = models.CharField(max_length=50, verbose_name="Cut", help_text="Cut of the diamond")
    color = models.CharField(max_length=1, verbose_name="Color", help_text="Color grade of the diamond")
    clarity = models.CharField(max_length=10, verbose_name="Clarity", help_text="Clarity grade of the diamond")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price", help_text="Price of the diamond")
    stock = models.IntegerField(verbose_name="Stock", help_text="Stock quantity of the diamond")
    certificate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Certificate", help_text="Certification details of the diamond")
    description = models.TextField(blank=True, null=True, verbose_name="Description", help_text="Description of the diamond")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Image URL", help_text="URL of the diamond image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Diamond"
        verbose_name_plural = "Diamonds"
        ordering = ['-created_at']
