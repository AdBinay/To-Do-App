from django.shortcuts import render
import requests
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def home(request):
    # Fetch data from the API
    response = requests.get('http://127.0.0.1:8000/api/todos/')
    
    # Convert the response to JSON
    todos = response.json()
    
    # Pass the data to the template
    return render(request, 'todo/home.html', {'todos': todos})
