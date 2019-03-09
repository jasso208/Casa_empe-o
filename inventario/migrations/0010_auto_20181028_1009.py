# Generated by Django 2.1.2 on 2018-10-28 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20181025_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion_Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=18)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('cp', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='direccion_envio',
            name='id_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Estado'),
        ),
        migrations.AddField(
            model_name='direccion_envio',
            name='id_municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.Municipio'),
        ),
        migrations.AddField(
            model_name='direccion_envio',
            name='id_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Pais'),
        ),
    ]