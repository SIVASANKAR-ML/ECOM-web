# Generated by Django 5.0.6 on 2024-08-24 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tags',
        ),
    ]
