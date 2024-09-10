from django.contrib import admin
from django.urls import path, include

from sclist.views import  DoneViewSet, InProgressViewSet, TodoDetailView, UpdateDoneStatus, UpdateInProgressStatus, UpdateTodayTaskStatus, UpdateTodoStatus,logout_view, LoginView, SignupView, TodoViewSet ,ContactViewSet,TodayTaskViewSet
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
    path('api/todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    
    path('todos/<int:todo_id>/update-status/', UpdateTodoStatus.as_view(), name='update-todo-status'),
    path('inprogress/<int:progress_id>/update-status/', UpdateInProgressStatus.as_view(), name='update-inprogress-status'),
    path('done/<int:done_id>/update-status/', UpdateDoneStatus.as_view(), name='update-done-status'),
    path('todaytasks/<int:task_id>/update-status/', UpdateTodayTaskStatus.as_view(), name='update-todaytask-status'),
]



