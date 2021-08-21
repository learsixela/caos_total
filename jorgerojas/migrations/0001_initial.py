# Generated by Django 3.2.6 on 2021-08-20 22:35

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteJRM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
                ('dv', models.CharField(max_length=1)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
