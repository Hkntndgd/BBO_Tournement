# Generated by Django 4.1.7 on 2023-02-20 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['play_date', 'group']},
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.tournament'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='JBmZieCo', max_length=8),
        ),
    ]