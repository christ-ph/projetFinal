from django.contrib import admin

from .models import Commande
from .models import Vente


@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = (
        "date_vente",
        "article",
        "client",
        "quantite",
        "prix",
        "total",
    )
    search_fields = (
        "article__nom_article",
        "client__nom",
        "client__prenom",
    )
    list_filter = ("date_vente", "article__categorie", "client")
    ordering = ("-date_vente",)
    list_per_page = 25
    date_hierarchy = "date_vente"
    autocomplete_fields = ("article", "client")  # champ avec autocomplétion
    list_select_related = ("article", "client")  # évite les requêtes N+1

    @admin.display(description="Total")
    def total(self, obj):
        return obj.quantite * obj.prix


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = (
        "date_commande",
        "article",
        "fournisseur",
        "quantite",
        "prix",
        "total",
    )
    search_fields = (
        "article__nom_article",
        "fournisseur__nom",
        "fournisseur__prenom",
    )
    list_filter = ("date_commande", "article__categorie", "fournisseur")
    ordering = ("-date_commande",)
    list_per_page = 25
    date_hierarchy = "date_commande"
    autocomplete_fields = ("article", "fournisseur")
    list_select_related = ("article", "fournisseur")

    @admin.display(description="Total")
    def total(self, obj):
        return obj.quantite * obj.prix
