from django.contrib import admin
from .models import CustomUser,Todo, Contact, TodayTask,InProgress,Done

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneNumber')
    search_fields = ('name', 'email', 'phoneNumber')
    list_filter = ('name',)  
    
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'delayed', 'description', 'user', 'status')
    search_fields = ('text', 'description', 'user__username')
    list_filter = ('delayed', 'status', 'user')

@admin.register(TodayTask)
class TodayTaskAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'delayed', 'description', 'user', 'status')
    search_fields = ('text', 'description', 'user__username')
    list_filter = ('delayed', 'status', 'user')

@admin.register(InProgress)
class InProgressAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'delayed', 'description', 'user', 'status')
    search_fields = ('text', 'description', 'user__username')
    list_filter = ('delayed', 'status', 'user')

@admin.register(Done)
class DoneAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'delayed', 'description', 'user', 'status')
    search_fields = ('text', 'description', 'user__username')
    list_filter = ('delayed', 'status', 'user')

    

    






    
    
