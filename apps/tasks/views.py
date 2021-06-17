from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import TasksSerializer
from .models import Tasks
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class TasksListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TasksSerializer)
    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)

            return HttpResponse(serializer.data['id'])
        return Response(serializer.errors)
