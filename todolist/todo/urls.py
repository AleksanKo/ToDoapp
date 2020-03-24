from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/',views.viewToDo, name='todos'),
    path('addToDo/',views.addToDo, name='add_todo'),
    path('deleteToDo/<int:todo_id>/',views.deleteToDo, name='delete_todo')
]