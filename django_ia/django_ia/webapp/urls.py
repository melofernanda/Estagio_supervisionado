from django.contrib import admin
from django.urls import path
from webapp.views import openai
from webapp.views import autenticacao

urlpatterns = [
    path("geral" , openai.geral, name="geral"),
    path("signin" , autenticacao.signin, name="signin"),
    path("signout" , autenticacao.signout, name="signout"),
    path("registro" , autenticacao.signup, name="registro"),
    path("historico" , openai.historico, name="historico"),
    path("deletar_registro/<id_do_registro>" , openai.deletar_registro, name="deletar_registro"),
]


