# Generated by Django 5.1 on 2024-09-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0021_todaytask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todaytask',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todaytask',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='todaytask',
            name='delayed',
            field=models.BooleanField(default=False),
        ),
    ]