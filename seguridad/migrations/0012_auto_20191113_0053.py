# Generated by Django 2.2.6 on 2019-11-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0011_recupera_pws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion_envio_cliente_temporal',
            name='numero_interior',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
