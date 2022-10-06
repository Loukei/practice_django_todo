from typing import Dict, List
from django.http import Http404, HttpRequest, HttpResponse
from django.template.loader import get_template
from django.template import Template
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Import todo app
from todo.models import TodoList, Todo
from todo.forms import TodoListForm

# Create your views here.
class DashboardView(LoginRequiredMixin, View):
    """
    TODO: change login_url when build a login page
    """
    login_url:str = 'admin/login/'
    redirect_field_name:str = 'redirect_to'
    http_method_names: List[str] = ["get"]

    def get(self, request:HttpRequest):
        """
        Display user dashboard
        1. show all user's todolist
        2. TODO add todolist form to context
        """
        lists = TodoList.objects.all()
        context:Dict = {'todo_lists': lists, 'todolistform': TodoListForm()}
        return render(request=request, template_name='todo_awesome/dashboard.html', context=context)