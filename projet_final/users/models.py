from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """
    Default custom user model for projet_final.
    """

    class Role(models.TextChoices):
        ADMIN = "admin", "Administrateur"
        EMPLOYE = "employe", "Employé"
        CLIENT = "client", "Client"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)
    telephone = models.CharField(max_length=20, blank=True)
    entreprise = models.CharField(max_length=100, blank=True)

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username
