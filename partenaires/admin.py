from django.contrib import admin

from .models import Client
from .models import Fournisseur


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "telephone", "adresse")
    search_fields = ("nom", "prenom", "telephone", "adresse")
    list_filter = ("nom", "prenom")  # filtres à droite
    ordering = ("nom", "prenom")
    list_per_page = 25

    fieldsets = (
        (
            "Identité",
            {
                "fields": ("nom", "prenom"),
            },
        ),
        (
            "Coordonnées",
            {
                "fields": ("telephone", "adresse"),
            },
        ),
    )


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "telephone", "adresse")
    search_fields = ("nom", "prenom", "telephone", "adresse")
    list_filter = ("nom", "prenom")
    ordering = ("nom", "prenom")
    list_per_page = 25

    fieldsets = (
        (
            "Identité",
            {
                "fields": ("nom", "prenom"),
            },
        ),
        (
            "Coordonnées",
            {
                "fields": ("telephone", "adresse"),
            },
        ),
    )
