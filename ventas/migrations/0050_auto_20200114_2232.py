# Generated by Django 2.2.6 on 2020-01-15 04:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0049_auto_20200113_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medio_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_medio', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 4, 32, 54, 183086, tzinfo=utc)),
        ),
    ]