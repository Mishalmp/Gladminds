# Generated by Django 5.0.2 on 2024-02-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_productimages_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
