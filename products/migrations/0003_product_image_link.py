# Generated by Django 4.0.6 on 2022-07-14 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_inventory_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.CharField(default=0, max_length=999),
            preserve_default=False,
        ),
    ]
