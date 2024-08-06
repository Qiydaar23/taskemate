from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
  
]