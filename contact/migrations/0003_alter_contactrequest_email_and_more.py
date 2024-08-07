# Generated by Django 5.0.6 on 2024-07-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contactrequest_name_contactrequest_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
