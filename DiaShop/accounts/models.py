from django.db import models

class Customer(models.Model):
    FullName = models.CharField(max_length=255, null=False)
    Email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    Phone = models.CharField(max_length=20, unique=True, null=False)
    Address = models.TextField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FullName
