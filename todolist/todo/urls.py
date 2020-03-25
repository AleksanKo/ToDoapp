from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/',views.addAndViewToDo, name='todos'),
    path('deleteToDo/<int:todo_id>/',views.deleteToDo, name='delete_todo'),
    path('completeToDo/<int:todo_id>/',views.completeToDo,name='complete_todo'),
    path('editToDo/<int:todo_id>/',views.completeToDo,name='edit_todo')
]