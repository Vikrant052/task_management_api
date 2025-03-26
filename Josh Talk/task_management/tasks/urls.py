from django.urls import path
from .views import (
    CreateTaskAPIView, AssignTaskAPIView, GetUserTasksAPIView, UpdateTaskStatusAPIView
)

urlpatterns = [
    path('create-task/', CreateTaskAPIView.as_view(), name='create-task'),
    path('assign-task/', AssignTaskAPIView.as_view(), name='assign-task'),
    path('user-tasks/<int:user_id>/', GetUserTasksAPIView.as_view(), name='user-tasks'),
    path('update-task-status/<int:task_id>/', UpdateTaskStatusAPIView.as_view(), name='update-task-status'),
]
