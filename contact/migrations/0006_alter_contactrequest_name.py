# Generated by Django 5.0.6 on 2024-07-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contactrequest_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
