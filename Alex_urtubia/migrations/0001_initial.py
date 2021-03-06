# Generated by Django 3.2.3 on 2021-08-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=12)),
                ('categoria', models.CharField(max_length=20)),
                ('distribuidor', models.CharField(max_length=50)),
                ('precio_venta', models.IntegerField(max_length=10)),
                ('costo', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
