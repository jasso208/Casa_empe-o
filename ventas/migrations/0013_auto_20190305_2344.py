# Generated by Django 2.1.2 on 2019-03-06 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_auto_20190304_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 23, 44, 46, 90234)),
        ),
    ]