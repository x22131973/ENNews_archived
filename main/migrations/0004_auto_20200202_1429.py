# Generated by Django 3.0.2 on 2020-02-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200202_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
