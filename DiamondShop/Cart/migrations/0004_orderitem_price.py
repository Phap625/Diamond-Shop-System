# Generated by Django 5.1.6 on 2025-02-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Cart", "0003_remove_orderitem_price_alter_order_total_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
