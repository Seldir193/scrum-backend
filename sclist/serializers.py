from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InProgress, Todo, Contact, TodayTask,Done
from .models import CustomUser

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  ['id', 'name', 'email', 'phoneNumber']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_staff = True 
        user.save()
        return user
       
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
class TodoSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Todo
        fields = ['id', 'text', 'delayed', 'description', 'user', 'contacts','status']
    
        read_only_fields = ['id','user']  
   
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        todo = Todo.objects.create(**validated_data)
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            todo.contacts.add(contact)
        return todo
    
    
    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.contacts.clear()
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            instance.contacts.add(contact)
        return instance


class TodayTaskSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = TodayTask
        fields = ['id','text', 'delayed', 'description', 'user', 'contacts','status']
        read_only_fields = ['id','user']  
   
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        task = TodayTask.objects.create(**validated_data)
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            task.contacts.add(contact)
        return task

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.contacts.clear()
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            instance.contacts.add(contact)
        return instance
    

class InProgressSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = InProgress
        fields = ['id', 'text', 'delayed', 'description', 'user', 'contacts','status']
        read_only_fields = ['id','user']  
   
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        progress = InProgress.objects.create(**validated_data)
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            progress.contacts.add(contact)
        return progress

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.contacts.clear()
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            instance.contacts.add(contact)
        return instance
    
class DoneSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Done
        fields = ['id', 'text', 'delayed', 'description', 'user', 'contacts','status']
        read_only_fields = ['id','user']  
   
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        done = Done.objects.create(**validated_data)
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            done.contacts.add(contact)
        return done
    
    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.contacts.clear()
        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            instance.contacts.add(contact)
        return instance