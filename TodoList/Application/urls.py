from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='create_account'),
    path('createtask', create_task, name='create_task'),
    path('gettasks', get_tasks, name='get_tasks')
]

