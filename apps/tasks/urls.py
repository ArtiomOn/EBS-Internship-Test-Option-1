from django.urls import path
from .views import TasksListView, TasksDetailView
urlpatterns = [
    path('tasks/', TasksListView.as_view()),
    path('tasks/<int:pk>/', TasksDetailView.as_view())
]