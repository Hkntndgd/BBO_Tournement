# Generated by Django 4.1.7 on 2023-02-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_scoreboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='week',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
