# Generated by Django 2.2.6 on 2020-01-28 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0103_auto_20200128_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 21, 8, 44, 178348, tzinfo=utc)),
        ),
    ]
