from django import forms
from .models import Vente, Commande


class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ["article", "client", "quantite", "prix"]


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["article", "fournisseur", "quantite", "prix"]
