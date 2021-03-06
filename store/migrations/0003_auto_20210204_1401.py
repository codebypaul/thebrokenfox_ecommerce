# Generated by Django 3.1.5 on 2021-02-04 14:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210202_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
