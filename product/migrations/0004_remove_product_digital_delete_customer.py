# Generated by Django 4.0.4 on 2022-07-22 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_shippingaddress_customer_and_more'),
        ('cart', '0003_remove_order_customer_order_user_info'),
        ('myorder', '0002_remove_myorder_customer'),
        ('product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
