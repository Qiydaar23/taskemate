from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    return render(request,'index.html')

def todolist(request):
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("A New Task Has Been Added!"))    
        return redirect('todolist')    
    else:    
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def contact(request):
    context = {
        'welcome_text': "welcome to contact List App"
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text': "welcome to About "
    }
    return render(request, 'about.html', context)

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method =="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))    
        return redirect('todolist')    
    else:    
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
