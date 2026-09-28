from django import forms

from projet_final.forms import StyledFormMixin

from .models import Commande
from .models import Vente


class VenteForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Vente
        fields = ["article", "client", "quantite", "prix"]


class CommandeForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["article", "fournisseur", "quantite", "prix"]
