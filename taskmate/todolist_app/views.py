from django.http import HttpResponse
from django.shortcuts import render


def todolist(request):
    context = {
        'welcome_text': "welcome to Todo List App"
    }
    return render(request, 'todolist.html', context)

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