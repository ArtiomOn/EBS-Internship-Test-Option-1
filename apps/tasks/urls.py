from django.urls import path
from .views import TasksListView
urlpatterns = [
    path('tasks/', TasksListView.as_view())
]