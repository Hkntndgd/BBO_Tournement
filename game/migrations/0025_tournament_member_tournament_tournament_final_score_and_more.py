# Generated by Django 4.1.7 on 2023-03-07 08:45

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_alter_member_options_alter_tournament_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='member',
            field=models.ManyToManyField(to='game.member'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_final_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='weekday',
            field=models.CharField(default='Tuesday', max_length=10, verbose_name='Match day'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='lgiDjTNC', max_length=24, verbose_name='Tournament name'),
        ),
    ]