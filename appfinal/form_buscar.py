from django import forms

class BuscaArtistaForm(forms.Form):
    artista = forms.CharField(max_length=30)