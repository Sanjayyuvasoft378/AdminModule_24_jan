# Generated by Django 3.2.16 on 2023-01-10 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_remove_payment_product_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]