from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoNode
from .forms import ToDoFormCreate, PersonCreate
#write a class

def login(request):
    return render(request,'login.html')

def index(request):
    form = PersonCreate()
    return render(request,'index.html',{'form':form})

def addP(request):
    pass

def viewToDo(request):
    all_todos = ToDoNode.objects.all()
    form = ToDoFormCreate()

    return render(request,'todo.html',{'form':form,'all_items':all_todos})

def addToDo(request):
    print('why')
    all_todos = ToDoNode.objects.all()
    if request.method == 'POST':
        form = ToDoFormCreate(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print('wow')
            return HttpResponseRedirect('/todo/')
    else:
        form = ToDoFormCreate()
        print('wtf')
    print('why')
    return render(request,'todo.html',{'form':form,'all_items':all_todos})

def editToDo(request):
    new_item = ToDoNode(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteToDo(request, todo_id):
    item_to_delete = ToDoNode.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
