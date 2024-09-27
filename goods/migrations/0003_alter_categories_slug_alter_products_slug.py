# Generated by Django 5.0.1 on 2024-09-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_rename_discout_products_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True, verbose_name='URL'),
        ),
    ]
