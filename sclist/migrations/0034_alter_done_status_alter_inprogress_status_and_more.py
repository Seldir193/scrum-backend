# Generated by Django 5.1 on 2024-09-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0033_done_status_inprogress_status_alter_done_contacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='done',
            name='status',
            field=models.CharField(choices=[('todos', 'To Do'), ('todaytasks', 'Today Tasks'), ('inProgress', 'In Progress'), ('done', 'Done')], default='done', max_length=50),
        ),
        migrations.AlterField(
            model_name='inprogress',
            name='status',
            field=models.CharField(choices=[('todos', 'To Do'), ('todaytasks', 'Today Tasks'), ('inProgress', 'In Progress'), ('done', 'Done')], default='inProgress', max_length=50),
        ),
        migrations.AlterField(
            model_name='todaytask',
            name='status',
            field=models.CharField(choices=[('todos', 'To Do'), ('todaytasks', 'Today Tasks'), ('inProgress', 'In Progress'), ('done', 'Done')], default='todaytasks', max_length=50),
        ),
    ]
