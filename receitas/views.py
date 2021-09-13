from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita
def index(request):
    receita = Receita.objects.order_by('-date_receita').filter(publicada=True) 
    #order_by('-date_receita') => Ordena por date_receita
    #   - => Da ultima postada para a primeira
    #filter(publicada=True) => filtra/pega/mostra apenas quando a publicada=True
    dados = {
        'receitas': receita
    }
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita' : receita
    }
    return render(request,'receita.html', receita_a_exibir)
