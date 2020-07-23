from django.db import models
from django.db.models import CASCADE


class Teste(models.Model):
    tipo = models.CharField(max_length=25)
    resultado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.tipo) + '- ' + str(self.resultado)


class Paciente(models.Model):
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateTimeField(auto_now_add=False)
    teste = models.ForeignKey(Teste, on_delete=CASCADE)
    
    def __str__(self):
        return str(self.nome) + '- ' + str(self.teste)
