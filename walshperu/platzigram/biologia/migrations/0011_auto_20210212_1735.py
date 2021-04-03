# Generated by Django 2.2.18 on 2021-02-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologia', '0010_auto_20210210_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='esfuerzo_muestreo_bd_mamiferos',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='esfuerzo_muestreo_bd_mamiferos',
            name='temporada',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='esfuerzo_muestreo_bd_mamiferos',
            name='unidad_vegetacion',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
