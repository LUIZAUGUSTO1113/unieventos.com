from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import uuid

# Create your views here.

# função responsável por redirecionar 127.0.0.1:8000 para 127.0.0.1:8000/welcome
def index(request):
    return HttpResponseRedirect('/welcome')

# função responsável por renderizar o template main.html no 127.0.0.1:8000/welcome
def welcome(request):
    return render(request, 'authentication/main.html')

# função responsável pela criação de usuários (127.0.0.1:8000/signup)
# caso usuário seja criado, essa função redireciona para 127.0.0.1:8000/signin
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # responsável também pela confirmação de senha
        if password != cpassword:
            messages.error(request, "As senhas não coincidem")
            return render(request, 'authentication/signup.html')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname

            myuser.save()

            messages.success(request, "Sua conta foi criada.")

            return redirect('/signin')

    return render(request, 'authentication/signup.html')

# função responsável por realizar o login do usuário cadastrado
# se as etapas de login forem sucedidas, redireciona para o app unieventos (127.0.0.1:8080/home)
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # autentica o usuário
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            email = user.email
            context = {
                'fname' : fname,
                'email' : email,
            }
            return redirect('unieventos:home')
        else:
            messages.error(request, "Credenciais erradas!")
            return redirect('/signin')

    return render(request, 'authentication/signin.html')

# função responsável pelo logout do usuário e retorno a 127.0.0.1:8000/welcome
def signout(request):
    logout(request)
    messages.success(request, "Desconectado com sucesso!")
    return redirect('/welcome')