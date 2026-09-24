from django.db import models

# Create your models here.
from django.db import models
from stock.models import Article
from partenaires.models import Client, Fournisseur

class Vente(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='ventes')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='ventes')
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateField(auto_now_add=True)
    

class Commande(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='commandes')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT, related_name='commandes')
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_commande = models.DateField(auto_now_add=True)
