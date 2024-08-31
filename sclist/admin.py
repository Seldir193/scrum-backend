from django.contrib import admin
from .models import CustomUser, Todo

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'delayed', 'order', 'user')  # Korrekte Felder für das Todo-Modell
    search_fields = ('text',)  # Suche nach dem 'text' Feld
    list_filter = ('delayed', 'user')  # Filter nach 'delayed' und 'user'
    ordering = ('order',)  # Sortierung nach 'order'

    

