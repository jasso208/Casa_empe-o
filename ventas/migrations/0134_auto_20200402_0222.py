# Generated by Django 2.2.6 on 2020-04-02 08:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0133_auto_20200401_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_cupon',
            name='usado',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 8, 22, 53, 456502, tzinfo=utc)),
        ),
    ]
