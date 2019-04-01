from rest_framework.serializers import ModelSerializer
from zappy_app.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'message', 'date')