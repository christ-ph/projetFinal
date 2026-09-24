from django.db import models

from partenaires.models import Client
from partenaires.models import Fournisseur

# Create your models here.
from stock.models import Article


class Vente(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
        related_name="ventes",
    )
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="ventes")
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.nom_article} vendue a {self.client.nom}"


class Commande(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
        related_name="commandes",
    )
    fournisseur = models.ForeignKey(
        Fournisseur,
        on_delete=models.PROTECT,
        related_name="commandes",
    )
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_commande = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.nom_article} forunit pas {self.fournisseur.nom}"
