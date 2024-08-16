from django import forms

class BuscaObraForm(forms.Form):
    obras = forms.CharField(max_length=300)