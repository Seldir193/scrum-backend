from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    # Hier können Sie zusätzliche Felder hinzufügen, falls erforderlich
    pass

class Todo(models.Model):
    text = models.CharField(max_length=255)
    delayed = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.text
    



