# Generated by Django 3.1.5 on 2021-02-10 19:09

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_item_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SignUpList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=255)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('default', models.BooleanField(default=False)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.imagealbum')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.imagealbum'),
        ),
    ]
