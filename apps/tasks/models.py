from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=False, verbose_name='Completed')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_assigned')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.assigned_to}'

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'


class Comment(models.Model):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'

