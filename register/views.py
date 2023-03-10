from django.shortcuts import render, redirect
from .register_form import RegisterForm
from .models import Register


def register(request):
    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


def success_register_page(request):
    return render(request, 'register/success_register.html')


def db_register(request):
    if request.method == 'POST':
        form = Register()
        form.first_name = request.POST.get('fname')
        form.last_name = request.POST.get('lname')
        form.username = request.POST.get('username')
        form.email = request.POST.get('email')
        form.password = request.POST.get('password')
        form.save()
        # redirecting, so it won't save same data in db multiple times when we refresh page
        return redirect('success_pg')
