# Generated by Django 2.2.6 on 2020-01-17 07:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0064_auto_20200117_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='talla',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='productos', chained_model_field='productos', on_delete=django.db.models.deletion.CASCADE, to='inventario.Tallas'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 17, 7, 45, 9, 897379, tzinfo=utc)),
        ),
    ]