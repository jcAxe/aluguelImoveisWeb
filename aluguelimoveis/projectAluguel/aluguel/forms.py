from django import forms
from aluguel.models import Imovel

class EnderecoForm(forms.Form):
    endereco = forms.CharField(label="Endereço",required=True)


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = "__all__"