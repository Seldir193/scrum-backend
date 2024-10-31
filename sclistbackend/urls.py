from django.contrib import admin
from django.urls import path, include
from sclist.views import TaskViewSet, ContactViewSet, logout_view, LoginView, SignupView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# API router for managing tasks and contacts
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # Endpoint for all task operations
router.register(r'contacts', ContactViewSet, basename='contact')  # Endpoint for all contact operations

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/login/', LoginView.as_view(), name='login'),  # User login
    path('api/logout/', logout_view, name='logout'),  # User logout
    path('api/register/', SignupView.as_view(), name='register'),  # User registration
    
    # JWT token management
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token request
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    
    # API router endpoints for tasks and contacts
    path('api/', include(router.urls)),  # Includes all URL routes for the registered viewsets
]
