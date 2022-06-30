# Generated by Django 4.0.4 on 2022-06-05 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_alter_customer_aadhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Aadhar',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(200000000000), django.core.validators.MaxValueValidator(999000000000)]),
        ),
    ]
