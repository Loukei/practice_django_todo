from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse
from django.template.loader import get_template
from django.template import Template
from .models import TodoList, Todo

# Create your views here.

def todo(request:HttpRequest):
    "display todo item"
    try:
        todo:Todo = Todo.objects.get(pk=1)
    except Todo.DoesNotExist:
        raise Http404("Todo object not found")
    return HttpResponse(f"todo: {todo.__str__()}")