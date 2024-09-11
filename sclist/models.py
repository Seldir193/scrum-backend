from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('todos', 'To Do'),
        ('todaytasks', 'Today Tasks'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    delayed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='todos')
    order = models.PositiveIntegerField(default=0)  # Für die Reihenfolge der Aufgaben

    def __str__(self):
        return f"{self.text} ({self.get_status_display()})"






    

    



