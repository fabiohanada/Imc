from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, Avaliacao

def home_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Pessoa.objects.create(nome=nome)
            return redirect('home')

    pessoas = Pessoa.objects.all()
    return render(request, 'home.html', {'pessoas': pessoas})

def calcular_imc_view(request, pessoa_id=None):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    
    if request.method == 'POST':
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        Avaliacao.objects.create(
            pessoa=pessoa,
            peso=peso,
            altura=altura
        )
        return redirect('calcular_imc', pessoa_id=pessoa.id)

    avaliacoes = Avaliacao.objects.filter(pessoa=pessoa)
    
    return render(request, 'calcular_imc.html', {
        'pessoa': pessoa,
        'avaliacoes': avaliacoes
    })
