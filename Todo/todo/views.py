from django.shortcuts import render, redirect

from todo.forms import TodoForm
from todo.models import Todo


# Create your views here.

# GET ALL
def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todo/todo_list.html', {"todos": todos})


# GET BY ID
def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todo/todo_detail.html', {"todo": todo})


# CREATE Todos from FORM
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {"form": form})


# UPDATE Todos
def todo_edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {"form": form})


# DONE Todos list
def done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, 'todo/done_list.html', {'dones': dones})


def todo_done(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todo_list')
