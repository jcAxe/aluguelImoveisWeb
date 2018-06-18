from django import forms
from aluguel.models import Imovel

class EnderecoForm(forms.Form):
    endereco = forms.CharField(label="Endereço",required=True)


class ImovelForm(forms.ModelForm):
    # categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True)
    # # nome = models.CharField(max_length=200, db_index=True)
    # slug = forms.CharField(label="Slug",required=True)
    # #imagem = forms.ImageField(upload_to='imoveis', blank=True)
    # imagem = forms.ImageField(label="Foto", required=True)
    # descricao = forms.CharField(label="Descrição", required=True)
    # dono =  forms.CharField(label="Dono", required=True)
    # preco = forms.DecimalField(max_digits=10, decimal_places=2)
    # numero = forms.IntegerField(label="Número", required=True)
    # rua = forms.CharField(label="Rua", required=True)
    # bairro = forms.CharField(label="Bairro",required=True)
    # cidade = forms.CharField(label="Cidade",required=True)
    # estado = forms.CharField(label="Estado",required=True)
    # pais = forms.CharField(label="País",required=True)
    # cep = forms.CharField(label="CEP",required=True)
    # #disponivel = forms.BooleanField(default=True)
    # #data_cadastramento = forms.DateTimeField(auto_now_add=True)
    # #data_atualizacao = forms.DateTimeField(auto_now=True)
    # endereco = forms.CharField(label="Endereço",required=True)
    class Meta:
        model = Imovel
        fields = "__all__"