from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoNode
from .forms import ToDoFormCreate
#write a class

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def viewToDo(request):
    all_todos = ToDoNode.objects.all()
    form = ToDoFormCreate()
    return render(request,'todo.html',{'form':form,'all_items':all_todos})

def addToDo(request):
    if request.method == 'POST':
        form = ToDoFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = ToDoFormCreate()
    return HttpResponseRedirect('/todo/')

def viewToDo(request):
    all_todos = ToDoNode.objects.all()
    all_not_completed_todos = ToDoNode.objects.filter(done=False)
    all_completed_todos = ToDoNode.objects.filter(done=True)
    form = ToDoFormCreate()
    return render(request,'todo.html',{'form':form,
                                       'all_items':all_todos,
                                       'all_not_completed_items':all_not_completed_todos,
                                       'all_completed_items':all_completed_todos})

def completeToDo(request, todo_id):
    item_to_complete = ToDoNode.objects.get(id = todo_id)
    item_to_complete.done = True
    item_to_complete.save()
    #print(item_to_complete.done, item_to_complete.id)
    return redirect('/todo/')

def editToDo(request, todo_id):
    edited_item = ToDoNode.objects.get(id = todo_id)
    edited_item.todo = 'LOL'
    edited_item.save()
    print(edited_item.done)
    return redirect('/todo/')

def deleteToDo(request, todo_id):
    item_to_delete = ToDoNode.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
