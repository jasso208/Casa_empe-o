# Generated by Django 2.1.2 on 2019-02-22 02:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0021_auto_20190221_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 20, 34, 1, 749235)),
        ),
    ]