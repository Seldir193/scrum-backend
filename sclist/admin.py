
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
    list_filter = ('name',)  # Füge Filter hinzu, falls relevant

#@admin.register(TodayTask)
#class TodayTaskAdmin(admin.ModelAdmin):
    #list_display = ('text', 'user', 'description', 'delayed')


#@admin.register(Contact)
#class ContactAdmin(admin.ModelAdmin):
    #list_display = ('name', 'email', 'phone_number')
    #search_fields = ('name', 'email')

#@admin.register(Todo)
#class TodoAdmin(admin.ModelAdmin):
    #list_display = ('text', 'delayed', 'order', 'user', 'description')
    #search_fields = ('text', 'description')
    #list_filter = ('delayed', 'user')
    #ordering = ('order',)
    
admin.site.register(Todo)
admin.site.register(TodayTask)
admin.site.register(InProgress)
admin.site.register(Done)





