# Generated by Django 3.2.16 on 2023-01-10 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_auto_20230110_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.product')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='adminapp.product')),
            ],
        ),
    ]