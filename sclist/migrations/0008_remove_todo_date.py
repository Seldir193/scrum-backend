# Generated by Django 5.1 on 2024-09-02 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0007_todo_date_todo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]
