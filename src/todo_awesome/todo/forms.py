from dataclasses import field
from django import forms
from .models import TodoList, Todo

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name','describe')
        widgets = {
            'name': forms.TextInput(attrs={'class':'NAMECLASS'}),
            'describe': forms.Textarea(attrs={'class':'DESCRIBECLASS'})
        }

class TodoForm(forms.Form):
    class Meta:
        model = Todo
        fields = ('name','describe')
        widgets = {
            'name': forms.TextInput(attrs={'class':'NAMECLASS'}),
            'describe': forms.Textarea(attrs={'class':'DESCRIBECLASS'})
        }