# Generated by Django 2.2.6 on 2020-01-26 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0040_estatus_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='publicado_ml',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='inventario.Estatus_Publicacion'),
        ),
    ]