from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Olá Mundo! Você está vendo o conteúdo da view index da aplicação 'vendas'")
    frase = "Olá mundo"
    return render(request, 'projectbase/index.html', {'frase': frase})

#def pagina1(request):
#    frase = "Você está na página 1"
#    return render(request, 'aluguel/pagina1.html', {'frase': frase})

def about(request):

    return render(request, 'projectbase/about.html')