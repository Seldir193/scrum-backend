# Generated by Django 5.1 on 2024-09-03 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0012_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
