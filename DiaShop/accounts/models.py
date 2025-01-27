from django.db import models

class Guest(models.Model):
    session_id = models.CharField(max_length=100, unique=True)  # SessionID
    created_at = models.DateTimeField(auto_now_add=True)  # CreatedAt

    class Meta:
        db_table = 'guest'

    def __str__(self):
        return f"Guest {self.id}"


class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Username
    full_name = models.CharField(max_length=100)  # FullName
    phone_number = models.CharField(max_length=15)  # PhoneNumber
    email = models.EmailField(blank=True, null=True)  # Email
    address = models.CharField(max_length=200, blank=True, null=True)  # Address
    password = models.CharField(max_length=255)  # Password
    created_at = models.DateTimeField(auto_now_add=True)  # CreatedAt
    guest = models.ForeignKey(
        Guest,
        on_delete=models.SET_NULL,  # ON DELETE SET NULL
        null=True,
        blank=True
    )  # GuestID

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.full_name}"
