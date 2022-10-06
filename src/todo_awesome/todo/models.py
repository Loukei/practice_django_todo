from pydoc import describe
from secrets import choice
from typing import List, Tuple
from django.db import models

# Create your models here.
class TodoList(models.Model):
    """
    """
    name = models.CharField(max_length=100,default="")
    describe = models.TextField(max_length=500,default="")
    
    def __str__(self) -> str:
        return f"{self.name}, {self.describe}"


class Todo(models.Model):
    "A vary basic Todo item model"
    TODO:str = 'TD'
    DOING:str = 'DI'
    DONE:str = 'DN'
    ABANDON:str = 'AD'
    STATUS_CHOICES:List[Tuple[str,str]] = [
        (TODO, 'Todo'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
        (ABANDON, 'Abandon'),
    ]
    name = models.CharField(max_length=100,default="")
    describe = models.CharField(max_length=500,default="")
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=TODO)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self) -> str:
        message:str = f"{self.name}, {self.status}, {self.list_id}"
        return message