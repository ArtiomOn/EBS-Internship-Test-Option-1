from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import TasksSerializer, TasksListSerializer, TasksDetailSerializer
from .models import Tasks
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class TasksListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TasksListSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TasksSerializer)
    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)

            return HttpResponse(serializer.data['id'])
        return Response(serializer.errors)


class TasksDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = TasksDetailSerializer(instance)
        return Response(serializer.data)
