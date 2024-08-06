# Generated by Django 5.0.6 on 2024-08-06 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_vendor_date_alter_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vender', to='core.vendor'),
        ),
    ]
