# Generated by Django 4.1.7 on 2023-03-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_alter_match_options_alter_match_weekday_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-play_date']},
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='zPtLJzcA', max_length=24, verbose_name='Tournament name'),
        ),
    ]
