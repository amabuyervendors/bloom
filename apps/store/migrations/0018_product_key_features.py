# Generated by Django 3.0.9 on 2020-10-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_category_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='key_features',
            field=models.TextField(blank=True, null=True),
        ),
    ]
