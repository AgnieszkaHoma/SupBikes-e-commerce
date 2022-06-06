# Generated by Django 4.0.1 on 2022-04-28 11:56

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProducts',
            field=models.CharField(max_length=200, null=True, verbose_name=backend.models.ShopCart),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='discountCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.discountcode'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='code',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.shippingaddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='priceForAll',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('B', 'Bikes'), ('C', 'Clothes'), ('A', 'Accessories'), ('Co', 'Components')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
