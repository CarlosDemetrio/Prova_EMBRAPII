from django.contrib import admin

from .models import Paciente, Teste

admin.site.register(Paciente)
admin.site.register(Teste)
