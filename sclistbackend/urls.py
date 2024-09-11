from django.contrib import admin
from django.urls import path, include
from sclist.views import TaskViewSet, ContactViewSet, logout_view, LoginView, SignupView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # Einheitliche Route für alle Tasks
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
    path('register/', SignupView.as_view(), name='register'),
]




