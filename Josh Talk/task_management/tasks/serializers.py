from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

class TaskAssignSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(child=serializers.IntegerField())

class TaskUpdateStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Task.STATUS_CHOICES)

    def validate_status(self, value):
        if value not in ['pending', 'in_progress', 'completed']:
            raise serializers.ValidationError("Invalid status.")
        return value
