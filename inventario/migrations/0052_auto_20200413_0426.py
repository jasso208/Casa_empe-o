# Generated by Django 2.2.6 on 2020-04-13 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0051_auto_20200219_2330'),
    ]

    operations = [
      
        migrations.AddField(
            model_name='tallas',
            name='apartado',
            field=models.IntegerField(default=0),
        ),
    ]
