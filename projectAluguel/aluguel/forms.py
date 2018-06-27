from django import forms

from aluguel.models import Imovel

class EnderecoForm(forms.Form):
    endereco = forms.CharField(label="Endereço",required=True)


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = (
            'rua', 'id', 'numero',
            'imagem', 'categoria',
            'cep','preco',
            'disponivel','endereco',
            'descricao',
        )
