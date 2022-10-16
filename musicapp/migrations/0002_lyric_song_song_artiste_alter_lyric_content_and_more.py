# Generated by Django 4.1.2 on 2022-10-16 05:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='Song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='Artiste',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
