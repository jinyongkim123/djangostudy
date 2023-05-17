from django.shortcuts import render, redirect
from .models import TodoItem

# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todolist_app/todo_list.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todolist_app/add_todo.html')