# Generated by Django 4.0.1 on 2022-06-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_date_added_orderitem_date_ordered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='complete',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userorder',
            name='is_ordered',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='userorder',
            name='items',
            field=models.ManyToManyField(to='backend.OrderItem'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='ref_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('B', 'Bikes'), ('C', 'Clothes'), ('A', 'Accessories'), ('H', 'Helmets'), ('Co', 'Components')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]