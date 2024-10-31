from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, TaskSerializer, ContactSerializer
from .models import Task, Contact
from .permissions import IsAdminOrReadOnly
from .utils import create_token_for_user, generate_jwt_tokens, authenticate_user


class SignupView(APIView):
    """Creates a new user and returns an authentication token."""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_key = create_token_for_user(user)
            return Response({
                'message': 'User registered successfully',
                'data': {
                    'username': user.username,
                    'email': user.email,
                    'token': token_key
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """Allows a user to log in and returns JWT tokens."""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate_user(username, password)

        if user:
            refresh_token, access_token = generate_jwt_tokens(user)
            return Response({
                'refresh': refresh_token,
                'access': access_token,
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Logs out the current user."""
    logout(request)
    return Response({'message': 'Logout successful'}, status=200)


class ContactViewSet(viewsets.ModelViewSet):
    """Provides CRUD functionality for contacts."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Provides CRUD functionality for tasks, restricted to the logged-in user."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TaskSerializer

    def get_queryset(self):
        """Shows only tasks for the current user, optionally filtered by status."""
        queryset = Task.objects.filter(user=self.request.user)
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def perform_create(self, serializer):
        """Assigns the current user as the task owner."""
        serializer.save(user=self.request.user)
