from django.shortcuts import render, redirect
from .models import TodoItem
# Create your views here.

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo = TodoItem.objects.create(title=title)
            return redirect('todo:todo_list')#url path 사용할 때 앱이름:pathname
        return redirect('todo:todo_list')