# Generated by Django 4.1.7 on 2023-03-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0023_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-tournament_score', 'username']},
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='xpHAdhBF', max_length=24, verbose_name='Tournament name'),
        ),
    ]