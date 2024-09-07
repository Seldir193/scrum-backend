from django.contrib.auth.models import AbstractUser
from django.db import models 
#import datetime

class CustomUser(AbstractUser):
    # Hier können Sie zusätzliche Felder hinzufügen, falls erforderlich
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    STATUS_CHOICES = [
        ('todo', 'ToDo'),
        ('todaytasks', 'TodayTasks'),
    ]
    
    
    
    text = models.CharField(max_length=255)
    delayed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Beispiel für ein Order-Feld
    #date = models.DateField( default=datetime.date.today)
    description = models.TextField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='todos', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
   
    

    def __str__(self):
        return f'({self.id}) {self.text}'


class TodayTask(models.Model):
    STATUS_CHOICES = [
        ('todo', 'ToDo'),
        ('todaytasks', 'TodayTasks'),
    ]
    
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    #contacts = models.ManyToManyField('Contact', blank=True)  # Assuming Contact is your existing model
    contacts = models.ManyToManyField(Contact, related_name='todaytasks', blank=True)
    #contacts = models.ManyToManyField(Contact)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    delayed = models.BooleanField(default=False)
    #contacts = models.ManyToManyField(Contact, related_name='todos', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todaytasks')

    def __str__(self):
        return self.text


class InProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    #contacts = models.ManyToManyField('Contact', blank=True)  # Assuming Contact is your existing model
    contacts = models.ManyToManyField(Contact, related_name='inprogress', blank=True)
    #contacts = models.ManyToManyField(Contact)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    delayed = models.BooleanField(default=False)
    #contacts = models.ManyToManyField(Contact, related_name='todos', blank=True)

    def __str__(self):
        return self.text


class Done(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    #contacts = models.ManyToManyField('Contact', blank=True)  # Assuming Contact is your existing model
    contacts = models.ManyToManyField(Contact, related_name='done', blank=True)
    #contacts = models.ManyToManyField(Contact)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    delayed = models.BooleanField(default=False)
    #contacts = models.ManyToManyField(Contact, related_name='todos', blank=True)

    def __str__(self):
        return self.text








    

    



