# Generated by Django 5.0.6 on 2024-07-24 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]
