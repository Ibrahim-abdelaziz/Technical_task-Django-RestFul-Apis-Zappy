from django.shortcuts import render
from rest_framework import viewsets
from . models import Task
from zappy_app.api.serializers import TaskSerializer
from django.http import HttpResponse
from rest_framework.response import Response
import json

# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def send_data(request):
    new_data = []
    data = ['array of object returned from twitter']
    new_data = json.loads(data)
    for data in new_data:
        print(new_data.append(data))
        data.save()
        return  new_data







