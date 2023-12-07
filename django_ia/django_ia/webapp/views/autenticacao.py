from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from webapp.forms import SignUpForm

def signin(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sucesso no login")
            return redirect("geral")
        else:
            messages.success(request, "Falha no login")
            return redirect("geral")
    return render(request, "geral.html")

def signout(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect("geral")

def signup(request):
    params = {
        "view":{
            "id": "registro",
            "titulo": "Registro de Usuário"
        },
    }
    if request.method == "POST":
        form = SignUpForm(request.POST)
        params["form"] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você criou uma conta com sucesso")
            return redirect("geral")
    else:
        params["form"] = SignUpForm()    
    return render(request, "registro.html", params)
