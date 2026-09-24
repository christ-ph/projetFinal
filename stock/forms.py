from django import forms

from projet_final.forms import StyledFormMixin

from .models import Article


class ArticleForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "nom_article",
            "categorie",
            "quantite",
            "prix_unitaire",
            "date_fabrication",
            "date_expiration",
        ]
        widgets = {
            "date_fabrication": forms.DateInput(attrs={"type": "date"}),
            "date_expiration": forms.DateInput(attrs={"type": "date"}),
        }
