# Generated by Django 4.1.7 on 2023-02-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_match_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='yHCPPDTM', max_length=8),
        ),
    ]
