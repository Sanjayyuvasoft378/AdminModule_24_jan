# Generated by Django 3.2.16 on 2023-01-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_rename_pro_name_payment_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adminapp.product'),
            preserve_default=False,
        ),
    ]
