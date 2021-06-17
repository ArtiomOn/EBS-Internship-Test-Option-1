from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.created_by}, {self.assigned_to}'

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'
