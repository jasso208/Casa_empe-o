# Generated by Django 2.1.2 on 2019-02-26 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0026_auto_20190225_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 21, 13, 40, 871931)),
        ),
        migrations.AlterUniqueTogether(
            name='atributos',
            unique_together={('id_producto', 'atributo')},
        ),
        migrations.AlterUniqueTogether(
            name='tallas',
            unique_together={('id_producto', 'talla')},
        ),
    ]