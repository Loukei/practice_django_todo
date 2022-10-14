from typing import Type, Optional, List, Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.template.loader import get_template
from django.template import Template
from django.urls import reverse as url_reverse
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

class TodoListCreate(View):
    """

    Args:
        View (_type_): _description_

    Returns:
        _type_: _description_
    """
    http_method_names: List[str] = ["post"]

    def post(self, request:HttpRequest):
        form:TodoListForm = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(redirect_to=url_reverse(viewname='dashboard'))

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