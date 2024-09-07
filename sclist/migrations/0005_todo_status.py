# Generated by Django 5.1 on 2024-09-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0004_remove_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('today', 'Today'), ('in-progress', 'In Progress'), ('done', 'Done')], default='today', max_length=20),
        ),
    ]