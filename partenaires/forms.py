from django import forms
from .models import Client, Fournisseur


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["nom", "prenom", "telephone", "adresse"]


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ["nom", "prenom", "telephone", "adresse"]
