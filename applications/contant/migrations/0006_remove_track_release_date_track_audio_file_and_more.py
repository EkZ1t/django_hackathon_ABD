# Generated by Django 4.2 on 2023-04-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contant', '0005_alter_track_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='release_date',
        ),
        migrations.AddField(
            model_name='track',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='track',
            name='audio_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]
