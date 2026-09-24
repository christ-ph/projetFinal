from django import forms

from projet_final.forms import StyledFormMixin

from .models import Client
from .models import Fournisseur


class ClientForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ["nom", "prenom", "telephone", "adresse"]


class FournisseurForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ["nom", "prenom", "telephone", "adresse"]
