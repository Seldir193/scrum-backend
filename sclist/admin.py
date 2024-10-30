from django.contrib import admin
from .models import CustomUser, Contact, Task

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneNumber')
    search_fields = ('name', 'email', 'phoneNumber')
    list_filter = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'text', 'delayed', 'description', 'user', 'status')
    search_fields = ('text', 'description', 'user__username')
    list_filter = ('delayed', 'status', 'user')


    






    
    
