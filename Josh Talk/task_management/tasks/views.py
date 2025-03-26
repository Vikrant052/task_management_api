from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer, TaskAssignSerializer, TaskUpdateStatusSerializer

class CreateTaskAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTaskAPIView(APIView):
    def post(self, request):
        serializer = TaskAssignSerializer(data=request.data)
        if serializer.is_valid():
            task = get_object_or_404(Task, id=serializer.validated_data['task_id'])
            users = User.objects.filter(id__in=serializer.validated_data['user_ids'])
            task.assigned_users.set(users)
            return Response({"message": "Task assigned successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserTasksAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateTaskStatusAPIView(APIView):
    def patch(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskUpdateStatusSerializer(data=request.data)

        if serializer.is_valid():
            task.status = serializer.validated_data['status']

            if task.status == 'completed':
                from django.utils.timezone import now
                task.completed_at = now()
            else:
                task.completed_at = None

            task.save()
            return Response({"message": "Task status updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
