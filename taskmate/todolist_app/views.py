from django.http import HttpResponse
from django.shortcuts import render
from .models import TaskList


def todolist(request):
    all_tasks = TaskList.objects.all()
 
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