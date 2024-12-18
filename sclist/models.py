from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Extends Django's AbstractUser for custom user attributes.
    """
    pass

class Contact(models.Model):
    """
    Stores contact information.
    
    Attributes:
        name (str): Contact's name.
        email (EmailField): Contact's email address.
        phone_number (str): Contact's phone number.
    """
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contacts", null=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        """Returns the contact's name."""
        return self.name

class Task(models.Model):
    """
    Represents a task with an optional description, contacts, and status.
    
    Attributes:
        STATUS_CHOICES (list): Choices for task status.
        user (ForeignKey): User assigned to the task.
        text (str): Task title.
        description (str, optional): Detailed description.
        contacts (ManyToManyField): Contacts associated with the task.
        delayed (bool): Marks task as delayed.
        status (str): Task status, based on STATUS_CHOICES.
        order (int): Position for ordering.
    """
    STATUS_CHOICES = [
        ('todos', 'To Do'),
        ('todaytasks', 'Today Tasks'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    CATEGORY_CHOICES = [
        ('Technical Tasks', 'Technical Tasks'),
        ('User Story', 'User Story')
    ]


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    delayed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='todos')
    order = models.PositiveIntegerField(default=0)  # Position for ordering
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Technical Tasks')

    def __str__(self):
        """Returns the task's title and status."""
        return f"{self.text} ({self.get_status_display()})"

