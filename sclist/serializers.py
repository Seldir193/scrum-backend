from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo
from .models import CustomUser




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
        user.is_staff = True  # Setzt den Staff-Status auf True
        user.save()
        return user
       
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    

    
#class LoginSerializer(serializers.Serializer):
    #email = serializers.EmailField()
    #password = serializers.CharField(write_only=True)
      
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


