from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('carat', models.DecimalField(max_digits=5, decimal_places=2)),
                ('clarity', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=models.CASCADE, to='your_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diamond', models.ForeignKey(on_delete=models.CASCADE, to='your_app.Diamond')),
                ('order', models.ForeignKey(on_delete=models.CASCADE, related_name='items', to='your_app.Order')),
            ],
        ),
    ]
