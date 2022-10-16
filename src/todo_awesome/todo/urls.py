from django.urls import path
from .views import todo, TodoListCreate, TodoListDetail

urlpatterns = [
    # ex:
    # path("todo", todo),
    # create a todolist
    path("todolist/create", TodoListCreate.as_view(), name='create_todolist'),
    # read a todolist
    path("todolist/<int:listid>", TodoListDetail.as_view(), name='search_todolist'),
    # # update a todolist
    # path("todolist/update/<int:listid>", , name='create_todolist'),
    # # delete a todolist
    # path("todolist/delete/<int:listid>", , name='create_todolist'),
]