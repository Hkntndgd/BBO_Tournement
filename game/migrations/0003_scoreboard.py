# Generated by Django 4.1.7 on 2023-02-16 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_tournament_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scoreboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.member')),
            ],
        ),
    ]
