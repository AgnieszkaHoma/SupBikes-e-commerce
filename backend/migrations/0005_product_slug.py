# Generated by Django 4.0.1 on 2022-05-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
