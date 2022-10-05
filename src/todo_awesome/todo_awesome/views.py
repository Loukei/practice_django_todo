from typing import List
from django.http import Http404, HttpRequest, HttpResponse
from django.template.loader import get_template
from django.template import Template
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashboardView(LoginRequiredMixin, View):
    """
    TODO: change login_url when build a login page
    """
    login_url:str = 'admin/login/'
    redirect_field_name:str = 'redirect_to'
    http_method_names: List[str] = ["get"]

    def get(self, request:HttpRequest):
        "Display user dashboard"
        
        return render(request=request, template_name='todo_awesome/dashboard.html', context={})