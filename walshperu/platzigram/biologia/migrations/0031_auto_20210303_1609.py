# Generated by Django 2.2.18 on 2021-03-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologia', '0030_auto_20210301_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_integrada_aves_chinalco_seca_2018',
            name='restringida_eba',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
