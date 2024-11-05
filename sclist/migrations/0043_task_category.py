# Generated by Django 5.1 on 2024-11-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0042_task_due_date_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Technical Tasks', 'Technical Tasks'), ('User Story', 'User Story')], default='Technical Tasks', max_length=50),
        ),
    ]