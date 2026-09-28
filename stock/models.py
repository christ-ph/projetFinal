from django.db import models

# Create your models here.


class Article(models.Model):
    nom_article = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_expiration = models.DateField(null=True, blank=True)
    date_fabrication = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nom_article
