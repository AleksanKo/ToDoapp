from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoNode

def viewToDo(request):
    all_todos = ToDoNode.objects.all()
    return render(request,'todo.html',{'all_items':all_todos})

def addToDo(request):
    new_item = ToDoNode(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteToDo(request, todo_id):
    item_to_delete = ToDoNode.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
