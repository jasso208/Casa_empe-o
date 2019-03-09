# Generated by Django 2.1.2 on 2019-02-22 03:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0023_auto_20190221_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='id_estatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='inventario.Estatus'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='id_proveedor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='inventario.Proveedor'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 21, 2, 18, 941551)),
        ),
    ]