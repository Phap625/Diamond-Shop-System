# Generated by Django 5.1.6 on 2025-02-15 07:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0005_alter_customer_password"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="password",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
        migrations.AddField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
