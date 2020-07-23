from django.forms import ModelForm
from .models import Paciente, Teste


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class TesteForm(ModelForm):
    class Meta:
        model = Teste
        fields = '__all__'
