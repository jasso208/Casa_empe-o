# Generated by Django 2.2.6 on 2020-01-28 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0105_auto_20200128_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 21, 14, 24, 602463, tzinfo=utc)),
        ),
    ]
