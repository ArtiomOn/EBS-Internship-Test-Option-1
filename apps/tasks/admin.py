from django.contrib import admin

from apps.tasks.models import Task, Comment


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'assigned_to')


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
