from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
    # Ventes
    path("ventes/", views.vente_list, name="vente_list"),
    path("ventes/nouvelle/", views.vente_create, name="vente_create"),
    path("ventes/<int:pk>/modifier/", views.vente_update, name="vente_update"),
    path("ventes/<int:pk>/supprimer/", views.vente_delete, name="vente_delete"),
    path("ventes/<int:pk>/detail", views.vente_detail, name="vente_detail"),
    path("ventes/nouveau/", views.create_vente, name="vente_create"),
    # Commandes
    path("commandes/", views.commande_list, name="commande_list"),
    path("commandes/nouvelle/", views.commande_create, name="commande_create"),
    path("commandes/<int:pk>/modifier/", views.commande_update, name="commande_update"),
    path(
        "commandes/<int:pk>/supprimer/",
        views.commande_delete,
        name="commande_delete",
    ),
]
