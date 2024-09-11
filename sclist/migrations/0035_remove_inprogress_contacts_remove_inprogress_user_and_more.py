# Generated by Django 5.1 on 2024-09-11 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclist', '0034_alter_done_status_alter_inprogress_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inprogress',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='inprogress',
            name='user',
        ),
        migrations.RemoveField(
            model_name='todaytask',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='todaytask',
            name='user',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('delayed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('todos', 'To Do'), ('todaytasks', 'Today Tasks'), ('inprogress', 'In Progress'), ('done', 'Done')], default='todos', max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
                ('contacts', models.ManyToManyField(blank=True, to='sclist.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Done',
        ),
        migrations.DeleteModel(
            name='InProgress',
        ),
        migrations.DeleteModel(
            name='TodayTask',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]