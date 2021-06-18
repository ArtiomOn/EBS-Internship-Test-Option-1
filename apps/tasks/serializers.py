from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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


class TasksUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['assigned_to']
