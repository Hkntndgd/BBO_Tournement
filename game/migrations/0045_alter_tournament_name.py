# Generated by Django 4.1.7 on 2023-03-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0044_alter_member_options_member_total_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='ddZEsqtS', max_length=24, verbose_name='Tournament name'),
        ),
    ]