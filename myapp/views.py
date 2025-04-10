from django.shortcuts import render
from django.http import JsonResponse 

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def home_view(request):
    """Return a welcome message."""
    return JsonResponse({'message': 'Welcome to the API!'})

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-created_at')  # Fetch all tasks
    serializer_class = TaskSerializer


class SecureHelloView(APIView):
    permission_classes = [IsAuthenticated]

def get(self, request):
    return Response({"message": f"Hello, {request.user.username}!"})
