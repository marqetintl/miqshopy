# Generated by Django 4.0.2 on 2022-07-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_is_oos'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_explicit',
            field=models.BooleanField(default=False, verbose_name='Exclude from facebook commerce feed'),
        ),
    ]
