from django.contrib import admin
from .models import CustomUser, Contact, Task
from rest_framework.authtoken.models import Token

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin configuration for CustomUser model."""
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    
   
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for Contact model."""
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for Task model."""
    list_display = ('text', 'delayed','category', 'description','priority', 'user', 'status', 'due_date')
    search_fields = ('text', 'description', 'user__username','category')
    list_filter = ('delayed', 'status', 'user','priority', 'due_date','category')






    
    
