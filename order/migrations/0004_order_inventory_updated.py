# Generated by Django 3.1.5 on 2021-04-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='inventory_updated',
            field=models.BooleanField(default=False),
        ),
    ]