# Generated by Django 3.0.5 on 2020-05-04 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20200504_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='cartId',
            new_name='cartID',
        ),
    ]
