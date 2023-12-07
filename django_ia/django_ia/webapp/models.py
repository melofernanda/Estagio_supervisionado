from django.db import models
from django.contrib.auth.models import User

class Registros(models.Model):
    choices = [
        ("geral", "geral"),
    ]
    user = models.ForeignKey(User, related_name="registros", on_delete=models.DO_NOTHING)
    pergunta = models.TextField(max_length=5000)
    comportamento = models.TextField(max_length=5000)
    resposta = models.TextField(max_length=5000)
    linguagem = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    tipo = models.CharField(max_length=50, choices=choices, null=True)