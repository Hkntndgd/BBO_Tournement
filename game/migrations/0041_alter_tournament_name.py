# Generated by Django 4.1.7 on 2023-03-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0040_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='EmPbWeGJ', max_length=24, verbose_name='Tournament name'),
        ),
    ]