# Generated by Django 3.0.10 on 2021-01-30 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20210129_2129'),
        ('order', '0009_auto_20200921_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ManyToManyField(related_name='orders', to='vendor.Vendor'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendor.Vendor'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor_paid',
            field=models.BooleanField(default=False),
        ),
    ]
