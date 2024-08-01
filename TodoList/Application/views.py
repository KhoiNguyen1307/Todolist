from django.shortcuts import render

# Create your views here.

from .forms import AccountForm, TaskForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task

@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = AccountForm(request.data)
        if form.is_valid():
            account = form.save()
            return Response({
                'message': 'Account created successfully',
                'account': {
                    'id': account.id,
                    'username': account.username,
                    'email': account.email,
                }
            },status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.data)
        if form.is_valid():
            task = form.save()
            return Response({
                'message': 'Task created successfully',
                'task': {
                    'id': task.id,
                    'userid': task.userid.id if task.userid else None, 
                    'description': task.description,
                    'startdate': task.startdate,
                    'enddate': task.enddate,
                    'level': task.level,
                    'status': task.status
                }
            },status=status.HTTP_201_CREATED)
        return Response(task.errrors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['GET'])
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return Response({
            'message': 'Get tasks successfully',
            'tasks': [
                {
                    'id': task.id,
                    'userid': task.userid.id if task.userid else None, 
                    'description': task.description,
                    'startdate': task.startdate,
                    'enddate': task.enddate,
                    'level': task.level,
                    'status': task.status
                } for task in tasks
            ]
            
        }, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)