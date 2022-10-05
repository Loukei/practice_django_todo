from django.urls import path
from .views import todo

urlpatterns = [
    # ex:
    path("todo", todo),
]