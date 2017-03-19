# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('cedula', models.CharField(unique=True, max_length=10)),
                ('telefono', models.CharField(unique=True, max_length=10)),
                ('correo', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(unique=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
                ('parada', models.ForeignKey(to='transporte.Parada')),
            ],
        ),
        migrations.CreateModel(
            name='RLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('id_est', models.ForeignKey(to='transporte.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='RutaVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_ruta', models.ForeignKey(to='transporte.Ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
                ('velocidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=7)),
                ('numero_gsm', models.CharField(unique=True, max_length=10)),
                ('codigo', models.CharField(unique=True, max_length=4)),
                ('estado', models.ForeignKey(to='transporte.Estado')),
                ('id_est', models.ForeignKey(to='transporte.Establecimiento')),
            ],
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
        migrations.AddField(
            model_name='rutavehiculo',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
        migrations.AddField(
            model_name='rline',
            name='id_ruta',
            field=models.ForeignKey(to='transporte.Ruta'),
        ),
        migrations.AddField(
            model_name='parada',
            name='id_ruta',
            field=models.ForeignKey(to='transporte.Ruta'),
        ),
        migrations.AddField(
            model_name='conductor',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
    ]
