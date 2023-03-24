# Generated by Django 4.1.7 on 2023-03-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0028_alter_match_weekday_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['last_name']},
        ),
        migrations.RemoveField(
            model_name='member',
            name='tournament_score',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='BrGWXPSm', max_length=24, verbose_name='Tournament name'),
        ),
    ]
