# Generated by Django 3.2.16 on 2022-12-15 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0005_alter_game_start_round_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'игра', 'verbose_name_plural': 'игры'},
        ),
        migrations.AlterModelOptions(
            name='gamemember',
            options={'verbose_name': 'участник', 'verbose_name_plural': 'участники'},
        ),
        migrations.AlterModelOptions(
            name='gamequestion',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
        migrations.AlterModelOptions(
            name='gameround',
            options={'verbose_name': 'раунд', 'verbose_name_plural': 'раунды'},
        ),
        migrations.AlterField(
            model_name='game',
            name='bank',
            field=models.IntegerField(default=0, verbose_name='банк'),
        ),
        migrations.AlterField(
            model_name='game',
            name='ended',
            field=models.BooleanField(default=False, verbose_name='игра закончена'),
        ),
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец игры'),
        ),
        migrations.AlterField(
            model_name='game',
            name='started',
            field=models.BooleanField(default=False, verbose_name='игра начата'),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='bad_answers',
            field=models.IntegerField(default=0, verbose_name='неправильных ответов'),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='brought_in_bank',
            field=models.IntegerField(default=0, verbose_name='принес в банк'),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game', verbose_name='игра'),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='good_answers',
            field=models.IntegerField(default=0, verbose_name='правильных ответов'),
        ),
        migrations.AlterField(
            model_name='gamemember',
            name='out_of_game',
            field=models.BooleanField(default=False, verbose_name='вылетел'),
        ),
        migrations.AlterField(
            model_name='gamequestion',
            name='answer',
            field=models.CharField(max_length=300, verbose_name='ответ'),
        ),
        migrations.AlterField(
            model_name='gamequestion',
            name='question',
            field=models.CharField(max_length=300, verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='bank',
            field=models.IntegerField(default=0, verbose_name='банк'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='время окончания'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='ended',
            field=models.BooleanField(default=False, verbose_name='раунд закончился'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='final',
            field=models.BooleanField(default=False, verbose_name='финальный раунд'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game', verbose_name='игра'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='now_bank',
            field=models.IntegerField(default=0, verbose_name='текущий банк'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='offset',
            field=models.IntegerField(default=0, verbose_name='номер отвечающего'),
        ),
        migrations.AlterField(
            model_name='gameround',
            name='vote',
            field=models.BooleanField(default=False, verbose_name='этап голосования'),
        ),
    ]
