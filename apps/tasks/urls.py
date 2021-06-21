from django.urls import path

from .views import (
    TaskCreateView,
    TaskDetailView,
    CurrentUserTasksDetailView,
    CompletedTasksListView,
    TaskUpdateAssignedUserDetailView,
    TaskUpdateStatusDetailView,
    CommentsDetailView,
    TaskFilterListView,
    CommentFilterListView
)

urlpatterns = [
    path('task/search/', TaskFilterListView.as_view()),
    path('task/comment/search/', CommentFilterListView.as_view()),
    path('task/', TaskCreateView.as_view()),
    path('task/user/', CurrentUserTasksDetailView.as_view()),
    path('task/completed/', CompletedTasksListView.as_view()),

    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('task/user/assigned/<int:pk>/', TaskUpdateAssignedUserDetailView.as_view()),
    path('task/update/status/<int:pk>/', TaskUpdateStatusDetailView.as_view()),
    path('task/comments/<int:pk>/', CommentsDetailView.as_view())
]
