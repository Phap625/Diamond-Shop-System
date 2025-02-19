from django.db import models
import os

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product_count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    def update_product_count(self):
        """Cập nhật số lượng sản phẩm trong danh mục"""
        self.product_count = self.product_set.count()
        self.save()

    def __str__(self):
        return f"{self.name} ({self.product_count} sản phẩm)"

def get_upload_path(instance, filename):
    category_name = instance.category.name.replace(" ", "_")
    product_name = instance.name.replace(" ", "_")
    return os.path.join(f'{category_name}/{product_name}/', filename)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    collection = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True, default='icon/default-product.jpg', max_length=255)
    sub_image1 = models.ImageField(upload_to=get_upload_path, null=True, blank=True, default='icon/default-product.jpg', max_length=255)
    sub_image2 = models.ImageField(upload_to=get_upload_path, null=True, blank=True, default='icon/default-product.jpg', max_length=255)
    sub_image3 = models.ImageField(upload_to=get_upload_path, null=True, blank=True, default='icon/default-product.jpg', max_length=255)
    weight = models.FloatField(help_text="Trọng lượng kim cương(carat)")
    sold = models.PositiveIntegerField(default=0, help_text="Số lượng sản phẩm đã bán")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.category.update_product_count()

    def delete(self, *args, **kwargs):
        category = self.category
        super().delete(*args, **kwargs)
        category.update_product_count()

    def __str__(self):
        return self.name
