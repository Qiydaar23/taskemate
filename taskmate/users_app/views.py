from django.shortcuts import redirect, render
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("new Account Created, Login and get Started"))
            return redirect('register')
    register_form = CustomRegisterForm()
    return render(request, 'login.html', {'register_form': register_form})