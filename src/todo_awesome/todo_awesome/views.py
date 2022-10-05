from django.http import Http404, HttpRequest, HttpResponse
from django.template.loader import get_template
from django.template import Template

# Create your views here.
def dashboard(request:HttpRequest):
    template:Template = get_template(template_name='todo_awesome/dashboard.html')
    return HttpResponse(template.render(context={},request=request))