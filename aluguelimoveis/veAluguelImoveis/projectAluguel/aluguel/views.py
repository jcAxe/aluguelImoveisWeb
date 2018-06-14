from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    # return HttpResponse("Olá Mundo! Você está vendo o conteúdo da view index da aplicação 'vendas'")
    frase = "Olá mundo"
    return render(request, 'aluguel/index.html', {'frase': frase})

def pagina1(request):
    frase = "Você está na página 1"
    return render(request, 'aluguel/pagina1.html', {'frase': frase})
def about(request):

    return render(request, 'aluguel/about.html')