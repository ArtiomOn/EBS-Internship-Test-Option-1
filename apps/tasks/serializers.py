from rest_framework.serializers import ModelSerializer

from apps.tasks.models import Task, Comment


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'assigned_to', 'assigned_to')
        extra_kwargs = {
            'assigned_to': {'read_only': True}
        }


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'assigned_to')


# And we use this serializer to find tasks status
class TaskCurrentUserSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title')


class TaskUpdateAssignedUserSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('assigned_to',)


class TaskUpdateStatusSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('status',)


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content')


class AllCommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
