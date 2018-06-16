from django import forms

class EnderecoForm(forms.Form):
    endereco = forms.CharField(label="Endereço",required=True)
