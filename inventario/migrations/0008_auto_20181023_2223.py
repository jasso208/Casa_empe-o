# Generated by Django 2.1.2 on 2018-10-24 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_carrito_compras'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_compras',
            name='talla',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='inventario.Tallas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrito_compras',
            name='session',
            field=models.CharField(max_length=14),
        ),
    ]