from rest_framework import serializers
from .models import Task, Contact, CustomUser

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phoneNumber']

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

class TaskSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'text', 'delayed', 'description', 'user', 'contacts', 'status']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        task = Task.objects.create(**validated_data)
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
