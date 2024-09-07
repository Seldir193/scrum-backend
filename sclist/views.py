from django.shortcuts import render
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, TodoSerializer, ContactSerializer,InProgressSerializer,DoneSerializer
from rest_framework import viewsets
from .models import  Todo ,Contact, TodayTask,InProgress,Done
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.views import LoginView as DjangoLoginView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from .serializers import TodayTaskSerializer

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'data': {
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=200)


class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TodoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class TodayTaskViewSet(viewsets.ModelViewSet):
    queryset = TodayTask.objects.all()
    serializer_class = TodayTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return TodayTask.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
        
   
        
class InProgressViewSet(viewsets.ModelViewSet):
    queryset = InProgress.objects.all()
    serializer_class = InProgressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return InProgress.objects.filter(user=self.request.user)
    
class DoneViewSet(viewsets.ModelViewSet):
    queryset = Done.objects.all()
    serializer_class = DoneSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Done.objects.filter(user=self.request.user)
    

    

    

    


