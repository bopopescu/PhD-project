# Generated by Django 2.1.7 on 2019-04-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighanalyzdatabase',
            name='out_time',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='neighanalyzdatabase',
            name='cut_off',
            field=models.CharField(max_length=9),
        ),
    ]