from django.shortcuts import render
from .login_form import LoginForm
from supabase import create_client
from database_creds import api_url, api_anon_pupblic_key


def signin(request):
    form = LoginForm()  # initiating form

    # pass the form to template by '{'form': form}'
    return render(request, 'sign_in/login.html', {'form': form})


def auth_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        supabase = create_client(api_url, api_anon_pupblic_key)
        db = supabase.table("register").select("username, password").execute()
        list_of_result = db.data
        for i in list_of_result:
            if username == i['username'] and password in i['password']:
                return render(request, 'sign_in/success_login.html')

        return render(request, 'sign_in/wrong_creds.html')


def logout(request):
    return render(request, 'home.html')
