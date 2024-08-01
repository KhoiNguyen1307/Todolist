from django import forms
from .models import Account, Task

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['userid', 'title', 'description', 'startdate', 'enddate', 'level', 'status']

