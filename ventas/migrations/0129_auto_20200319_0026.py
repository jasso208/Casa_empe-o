# Generated by Django 2.2.6 on 2020-03-19 06:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0128_auto_20200312_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 6, 26, 51, 791020, tzinfo=utc)),
        ),
    ]
