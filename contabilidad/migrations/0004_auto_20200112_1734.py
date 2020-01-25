# Generated by Django 2.2.6 on 2020-01-12 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20200112_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movs_gasto',
            name='id_v',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ventas.Venta'),
        ),
        migrations.AlterField(
            model_name='movs_ingreso',
            name='id_v',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ventas.Venta'),
        ),
    ]