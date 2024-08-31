
from django.contrib import admin
from django.urls import path, include
from sclist.views import  logout_view,  TodoViewSet, LoginView, SignupView
from rest_framework.routers import DefaultRouter
#from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('register/', register, name='register'),
    #path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'), 
    path('api/', include(router.urls)),
    path('register/', SignupView.as_view(), name='register'),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   
]
