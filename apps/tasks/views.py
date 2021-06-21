from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.tasks.models import Task
from apps.tasks.serializers import (
    TaskCreateSerializer,
    TaskCurrentUserSerializer,
    TaskDetailSerializer,
    TaskUpdateAssignedUserSerializer,
    TaskUpdateStatusSerializer,
    CreateCommentSerializer,
    AllCommentsSerializer
)


class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskCurrentUserSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TaskCreateSerializer)
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_to=request.user)
            return Response(serializer.data['id'])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = TaskDetailSerializer(instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)


class CurrentUserTasksDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = TaskCurrentUserSerializer(tasks, many=True)
        return Response(serializer.data)


class CompletedTasksListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(status=True)
        serializer = TaskCurrentUserSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskUpdateAssignedUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=TaskUpdateAssignedUserSerializer)
    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = TaskUpdateAssignedUserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUpdateStatusDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=TaskUpdateStatusSerializer)
    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = TaskUpdateStatusSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        instance: Task = self.get_object(pk)
        serializer = AllCommentsSerializer(instance.comments, many=True)
        return Response(serializer.data)

    # Error ---
    @swagger_auto_schema(request_body=CreateCommentSerializer)
    def post(self, request, pk):
        instance = self.get_object(pk)
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=instance)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
