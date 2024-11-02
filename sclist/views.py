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
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import random
from django.utils.timezone import now
from django.db.models import Count


def create_unique_guest_user():
    """Creates a unique guest user with a random username."""
    CustomUser = get_user_model()
    while True:
        random_id = random.randint(1000, 9999)
        guest_username = f"guest_{random_id}"
        if not CustomUser.objects.filter(username=guest_username).exists():
            break
    
    # Create the guest user with a unique username
    guest_user = CustomUser.objects.create_user(username=guest_username, password="guestpassword")
    guest_user.is_staff = False  # Optional: set permissions as needed
    guest_user.save()

    # Create and return an authentication token for the guest user
    token, _ = Token.objects.get_or_create(user=guest_user)
    return guest_user, token

class GuestLoginView(APIView):
    """Logs in as a unique guest user and returns JWT tokens."""
    permission_classes = [AllowAny]

    def post(self, request):
        # Create a unique guest user
        guest_user, token = create_unique_guest_user()
        refresh_token, access_token = generate_jwt_tokens(guest_user)
        
        return Response({
            'username': guest_user.username,
            'refresh': refresh_token,
            'access': access_token,
            'token': token.key,
        })

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



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_summary(request):
    """Returns task summary information."""
    user = request.user

    # 1. Last task creation date
    last_task = Task.objects.filter(user=user).order_by('-id').first()
    last_task_date = last_task.created_at if last_task else None

    # 2. Total task count
    total_tasks = Task.objects.filter(user=user).count()

    # 3/4/5/6. Count of tasks by status
    task_status_counts = Task.objects.filter(user=user).values('status').annotate(count=Count('id'))
    
    # Organize counts by status in a dictionary
    status_count_dict = {
        "todos": 0,
        "todaytasks": 0,
        "inprogress": 0,
        "done": 0
    }
    
    # Populate the dictionary with counts
    for item in task_status_counts:
        status_count_dict[item['status']] = item['count']

    # Combine all data into a single response
    data = {
        "last_task_date": last_task_date,
        "total_tasks": total_tasks,
        "status_counts": status_count_dict
    }
    
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    """Returns the current user's information."""
    user = request.user
    return Response({'username': user.username})


class ContactViewSet(viewsets.ModelViewSet):
    """Provides CRUD functionality for contacts."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        """
        Returns only the contacts that belong to the authenticated user.
        """
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
       """
       Set the current user as the owner of the contact.
       """
       serializer.save(user=self.request.user)

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
        
   


