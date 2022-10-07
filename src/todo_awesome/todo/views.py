from typing import Type, Optional
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.template.loader import get_template
from django.template import Template
from .models import TodoList, Todo
from .forms import TodoListForm

# Create your views here.

def todo(request:HttpRequest):
    "display todo item"
    try:
        todo:Todo = Todo.objects.get(pk=1)
    except Todo.DoesNotExist:
        raise Http404("Todo object not found")
    return HttpResponse(f"todo: {todo.__str__()}")

# class TodoListCreateView(CreateView):
#     """
#     An API accept client command to create a todo list
#     ---
#     Model: TodoList
#     template_name
#     ---
#     ## Input
#     Endpoint: "user/<int:userid>/CreateTodoList"
#     Method: POST
#     Trigger by: User DashboardView, when user click "add new List" button
#     ---
#     ## Response
#     - 200 ok
#     """
#     model: Type[models.Model] = TodoList
#     template_name: str = ''
#     form_class: Optional[Type[BaseForm]] = TodoListForm

#     def get_success_url(self) -> str:
#         "TODO: redirect user to dashboard"
#         return super().get_success_url()

# class TodoListListView(ListView):
#     """
#     An API to show User's todolist
#     ---
#     Model: TodoList
#     template_name
#     ---
#     Endpoint: "user/<int:userid>/"
#     Method: GET
#     Response: 
#         - URL: "Dashboard/"
#     Trigger by: User DashboardView
#     """

# class TodoCreateView(CreateView):
#     model = Todo
#     form_class = 