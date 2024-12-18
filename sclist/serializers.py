from rest_framework import serializers
from .models import Task, Contact, CustomUser
from .utils import create_token_for_user, generate_jwt_tokens, authenticate_user


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for Contact model with fields for contact data display and storage."""
    
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone_number']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Benutzer aus Anfrage setzen
        return super().create(validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration with required fields for creating a new user."""
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate_email(self, value):
        """Ensure the email is unique."""
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Diese E-Mail-Adresse wird bereits verwendet.")
        return value

    def create(self, validated_data):
        """Creates a new user with superuser and staff permissions."""
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login capturing username and password fields."""
    
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model including associated contacts for task creation and update."""
    
    contacts = ContactSerializer(many=True)
    
    due_date = serializers.DateField(required=False, allow_null=True)
   
    

    class Meta:
        model = Task
        fields = ['id', 'text', 'delayed', 'description', 'user', 'contacts','category', 'status','priority','due_date']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        """Creates a new task and associates specified contacts."""
        contacts_data = validated_data.pop('contacts', [])
        task = Task.objects.create(**validated_data)
        self.add_contacts_to_task(task, contacts_data)
        return task

    def update(self, instance, validated_data):
        """Updates an existing task and its associated contacts."""
        contacts_data = validated_data.pop('contacts', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.contacts.clear()
        self.add_contacts_to_task(instance, contacts_data)
        return instance
    
    def add_contacts_to_task(self, task, contacts_data):
        """Helper method to add contacts to a task, scoped to the user's contacts."""
        for contact_data in contacts_data:
            # Benutzer hinzufügen, um sicherzustellen, dass der Kontakt eindeutig für den Benutzer ist
            contact, created = Contact.objects.get_or_create(
                user=task.user,  # Benutzer festlegen
                **contact_data
            )
            task.contacts.add(contact)






    
