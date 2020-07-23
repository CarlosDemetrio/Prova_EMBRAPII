from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Teste
from .Form import PacienteForm, TesteForm

@login_required
def home(request):
    return render(request, 'AppCovid/index.html')


@login_required
def lista_pacientes(request):
    paciente = Paciente.objects.all()
    form = PacienteForm()
    return render(request, 'AppCovid/lista/lista_pacientes.html', {'Paciente': paciente, 'form': form})


@login_required
def lista_testes(request):
    teste = Teste.objects.all()
    form = PacienteForm()
    return render(request, 'AppCovid/lista/lista_testes.html', {'Teste': teste, 'form': form})


@login_required
def paciente_novo(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_paciente')


@login_required
def testes_novo(request):
    form = TesteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_testes')


@login_required
def paciente_update(request, id):
    data = {}
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    data['paciente'] = paciente
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('lista_paciente')
    else:
        return render(request, 'AppCovid/update/update_paciente.html', data, id)


@login_required
def testes_update(request, id):
    data = {}
    teste = Teste.objects.get(id=id)
    form = TesteForm(request.POST or None, instance=teste)
    data['teste'] = teste
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('lista_testes')
    else:
        return render(request, '', data, id)
    
    
@login_required
def paciente_delete(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_paciente')


@login_required
def testes_delete(request, id):
    teste = Teste.objects.get(id=id)
    if request.method == 'POST':
        teste.delete()
        return redirect('lista_testes')

