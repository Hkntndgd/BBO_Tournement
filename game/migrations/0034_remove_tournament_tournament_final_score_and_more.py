# Generated by Django 4.1.7 on 2023-03-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0033_alter_tournament_name_alter_tournament_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='tournament_final_score',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='EanuBwcb', max_length=24, verbose_name='Tournament name'),
        ),
    ]