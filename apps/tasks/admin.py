from django.contrib import admin
from .models import Tasks

# Register your models here.
#admin.site.register(Tasks)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'created_by', 'assigned_to']
