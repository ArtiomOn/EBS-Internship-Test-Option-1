from django.urls import path
from .views import (
    TasksListView,
    AllTasksDetailView,
    UsersTasksDetailView,
    CompletedTasksListView,
    AssignTaskUserDetailView
)

urlpatterns = [
    path('tasks/', TasksListView.as_view()),
    path('tasks/<int:pk>/', AllTasksDetailView.as_view()),
    path('tasks/users/', UsersTasksDetailView.as_view()),
    path('tasks/done/', CompletedTasksListView.as_view()),
    path('update/<int:pk>/', AssignTaskUserDetailView.as_view())
]
