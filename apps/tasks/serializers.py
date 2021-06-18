from rest_framework.serializers import ModelSerializer
from .models import Tasks


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'assigned_to', 'created_by')
        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class TasksListSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title')


class TasksDetailSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'assigned_to', 'created_by')


class TasksUpdateAssignedUserSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['assigned_to']


class TasksUpdateOwnerUserSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['created_by']


class TasksUpdateStatusSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['status']
