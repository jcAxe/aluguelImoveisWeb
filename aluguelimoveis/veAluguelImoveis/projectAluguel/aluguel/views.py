from aluguel.forms import ContactForm
from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404
from .models import Categoria, Imovel



def lista_imoveis(request, slug_da_categoria=None):
    categoria = None
    proximidade = False
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        imoveis = imoveis.filter(categoria=categoria)

    return render(request, 'aluguel/imovel/lista.html', {'categorias': categorias,
                                                         'imoveis': imoveis,
                                                         'categoria': categoria,
                                                         'proximidade': proximidade})
def lista_proximidade(request):
    latitude = None
    longitude = None
    categoria = None
    proximidade = True
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print
            form.cleaned_data['formLatitude']
            form.cleaned_data['formLongitude']
            #return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
        pass

    return render(request, 'aluguel/imovel/lista.html', {'categorias': categorias,
                                                         'imoveis': imoveis,
                                                         'categoria': categoria,
                                                         'proximidade':proximidade,
                                                         'latitude': latitude,
                                                         'longitude': longitude})
def exibe_imovel(request, id, slug_do_imovel):
    # Esta view espera receber o id do produto e seu slug para recuperar o produto
    # Podemos recuperar o produto apenas com o seu id uma vez que ele é unique.
    # Incluímos o slug para podermos construir 'SEO friendly URLs'.
    # SEO = Search Engine Optimization.
    # Exemplo: http://www.dominio.com.br/produto?id=721 <== Ruim
    # Exemplo: http://www.dominio.com.br/721/notebook-del-vostro-3458-i3 <== Bom
    imovel = get_object_or_404(Imovel, id=id, slug=slug_do_imovel, disponivel=True)
    return render(
        request, 'aluguel/imovel/exibe.html', {'imovel': imovel})