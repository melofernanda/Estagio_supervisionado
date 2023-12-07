from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from webapp.models import Registros

OPENAI_KEY = "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"


def geral(request):
    params = {
        "view": {
            "id": "geral",
            "titulo": "Perguntas"
        },
        
    }
    if request.method == "POST":
        params["code1"] = request.POST["code1"]
        params["code"] = request.POST["code"]
        messages = [
            {"role": "system", "content": params["code1"]},
            {"role": "user", "content": params["code"]}
        ]
        #Aqui é o request para a openia
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            params["response"] = response["choices"][0].message["content"]
             #Salva o registro no histórico
            registro = Registros(
                pergunta=params["code"],
                comportamento=params["code1"],
                resposta=params["response"],
                linguagem="geral",
                user=request.user,
                tipo=params["view"]["id"],
            )
            registro.save()
        except Exception as e:
            params["code"] = e
    return render(request, "geral.html", params)

def historico(request):
    registros = Registros.objects.filter(user_id=request.user.id)
    params = {
        "titulo": "Historico",
        "registros": registros
    }
    
    return render(request, "historico.html", params) 


def deletar_registro(request, id_do_registro):
    registro = Registros.objects.get(pk=id_do_registro)
    registro.delete()
    messages.success(request, "Registro apagado")
    return redirect("historico")

