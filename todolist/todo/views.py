import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import ToDoNode
from .forms import ToDoFormCreate

def login(request):
    return render(request,'login.html')

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def addToDo(request):
     if request.method == 'POST':
         form = ToDoFormCreate(request.POST)
         if form.is_valid():
             t = ToDoNode(todo = form.cleaned_data['todo'], user=request.user)
             t.save()
             return redirect('/todo/')
     else:
         form = ToDoFormCreate()
     return redirect('/todo/')

@login_required
def viewToDo(request):
    all_todos = ToDoNode.objects.filter(user=request.user)
    all_not_completed_todos = all_todos.filter(done=False)
    all_completed_todos = all_todos.filter(done=True)
    form = ToDoFormCreate()
    return render(request,'todo.html',{'form':form,
                                       'all_items':all_todos,
                                       'all_not_completed_items':all_not_completed_todos,
                                       'all_completed_items':all_completed_todos})

@login_required
def completeToDo(request, todo_id):
    item_to_complete = ToDoNode.objects.get(id = todo_id)
    item_to_complete.done = True
    item_to_complete.save()
    #print(item_to_complete.done, item_to_complete.id)
    return redirect('/todo/')

@login_required
def editToDo(request, todo_id):
    edited_item = ToDoNode.objects.get(id = todo_id)
    edited_item.todo = 'LOL'
    edited_item.save()
    print(edited_item.done)
    return redirect('/todo/')

@login_required
def deleteToDo(request, todo_id):
    item_to_delete = ToDoNode.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')