from typing import Type, Optional, List, Any, Dict
from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import View
# from django.template.loader import get_template
# from django.template import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as auth_LoginView
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
    Create User's todolist, than return to {DashboardView}
    
    trigger by {dashboard.html sidebar_todolist_create_form}
    Args:
        View (_type_): _description_

    Returns:
        _type_: _description_
    """
    http_method_names: List[str] = ["post"]

    def post(self, request:HttpRequest):
        form:TodoListForm = TodoListForm(request.POST)
        if form.is_valid():
            list:TodoList = form.save()
        return HttpResponseRedirect(redirect_to=url_reverse(viewname='dashboard'))

class TodoListDetail(LoginRequiredMixin, View):
    login_url: Any = 'admin/login/'
    redirect_field_name:str = 'redirect_to'
    http_method_names: List[str] = ['get']

    def get(self, request:HttpRequest, listid:int)->HttpResponse:
        """
        If client is authenticated and has autheraction to listid, get todolist(listid)
        Return Dashboard.html with todolist
        """
        current_list:TodoList = TodoList.objects.get(pk=listid)
        lists = TodoList.objects.all()
        context:Dict = {'todo_lists': lists, 'todolistform': TodoListForm(), "current_list":current_list}
        return render(request=request,template_name='todo_awesome/dashboard.html',context=context)


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