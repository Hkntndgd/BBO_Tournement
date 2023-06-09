# Generated by Django 4.1.7 on 2023-03-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0030_alter_member_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='members',
            new_name='players',
        ),
        migrations.AlterField(
            model_name='match',
            name='weekday',
            field=models.CharField(default='Tuesday', max_length=10, verbose_name='Match day'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='gJVitaSC', max_length=24, verbose_name='Tournament name'),
        ),
    ]
