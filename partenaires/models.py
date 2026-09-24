from django.db import models

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="client_profile",
        null=True,
        blank=True,
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
