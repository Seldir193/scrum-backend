from django.contrib import admin
from django.urls import path, include

from sclist.views import  DoneViewSet, InProgressViewSet, logout_view, LoginView, SignupView, TodoViewSet ,ContactViewSet,TodayTaskViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
#router.register(r'todos', TodoViewSet)
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'todaytasks', TodayTaskViewSet, basename='todaytask')
router.register(r'inprogress', InProgressViewSet, basename='inprogress')
router.register(r'done', DoneViewSet, basename='done')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'), 
    path('api/', include(router.urls)),
    path('register/', SignupView.as_view(), name='register'),
    
]



