
from django.shortcuts import render

# Create your views here.
def  home (request):
    return render(request,'base/home.html')

def  classificacao (request):
    return render(request,'base/classificacao.html')

def  perguntas (request, indice):
    contexto ={'indice_da_questao':indice}
    return render(request,'base/game.html', context=contexto)

