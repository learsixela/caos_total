# Generated by Django 3.2.6 on 2021-08-21 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('david_mix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]