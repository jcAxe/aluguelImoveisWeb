from django import forms

class ContactForm(forms.Form):
    latitude = forms.CharField(required=True)
    longitude = forms.CharField(required=True)