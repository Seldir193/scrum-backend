# Generated by Django 5.1 on 2024-09-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0002_alter_todo_order_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('TO-DO', 'To-Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TO-DO', max_length=20),
        ),
    ]