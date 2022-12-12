# Generated by Django 3.2.16 on 2022-12-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20221212_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='end_round_time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='name',
            field=models.CharField(max_length=30, verbose_name='имя'),
        ),
    ]
