from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import filters

from apps.tasks.models import Task, Comment
from django.conf import settings
from apps.tasks.serializers import (
    TaskCreateSerializer,
    TaskCurrentUserSerializer,
    TaskDetailSerializer,
    TaskUpdateAssignedUserSerializer,
    TaskUpdateStatusSerializer,
    CreateCommentSerializer,
    AllCommentsSerializer
)


class TaskFilterListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^id', '^title', '^description', '^status']


class CommentFilterListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^id', '^content']


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

    def get(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskDetailSerializer(instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
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

    @swagger_auto_schema(request_body=TaskUpdateAssignedUserSerializer)
    def patch(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskUpdateAssignedUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.assigned_to = serializer.validated_data.get('assigned_to')
        instance.save()
        self.send_task_assigned_email(instance.id, instance.assigned_to.email)
        return Response(status=status.HTTP_200_OK)

    @classmethod
    def send_task_assigned_email(cls, task_id, user_email):
        send_mail('Task is assigned',
                  f'Task {task_id} is assigned to you', settings.EMAIL_HOST_USER, [user_email], fail_silently=False)


class TaskUpdateStatusDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=TaskUpdateStatusSerializer)
    def patch(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskUpdateStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.send_task_completed_email(instance.id, instance.assigned_to.email)
        return Response(status=status.HTTP_200_OK)

    @classmethod
    def send_task_completed_email(cls, task_id, user_email):
        send_mail('Task is updated',
                  f'Task {task_id} status in updated', settings.EMAIL_HOST_USER, [user_email], fail_silently=False)


class CommentsDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        instance: Task = get_object_or_404(Task, pk=pk)
        serializer = AllCommentsSerializer(instance.comments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CreateCommentSerializer)
    def post(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(task=instance)
        self.send_task_commented_email(instance.id, instance.assigned_to.email)
        return Response(serializer.data)

    @classmethod
    def send_task_commented_email(cls, task_id, user_email):
        send_mail('Task is commented',
                  f'Task {task_id} is commented', settings.EMAIL_HOST_PASSWORD, [user_email], fail_silently=False)
