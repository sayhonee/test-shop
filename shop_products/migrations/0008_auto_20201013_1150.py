# Generated by Django 3.1.2 on 2020-10-13 08:20

from django.db import migrations, models
import shop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0007_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'تصویر', 'verbose_name_plural': 'گالری تصویر'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to=shop_products.models.upload_galleries_image_path, verbose_name='عکس'),
        ),
    ]
