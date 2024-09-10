from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Hier können Sie zusätzliche Felder hinzufügen, falls erforderlich
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class BaseTask(models.Model):
    STATUS_CHOICES = [
        ('todos', 'To Do'),
        ('todaytasks', 'Today Tasks'),
        ('inProgress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    delayed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='todos')

    class Meta:
        abstract = True

    def __str__(self):
        return self.text

class Todo(BaseTask):
    order = models.PositiveIntegerField(default=0)

class TodayTask(BaseTask):
    pass

class InProgress(BaseTask):
    pass

class Done(BaseTask):
    pass









    

    



