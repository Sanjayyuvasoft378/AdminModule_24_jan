# Generated by Django 3.2.13 on 2023-01-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_payment_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='subscription_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
