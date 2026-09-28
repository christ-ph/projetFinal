from django.urls import path

from . import views

app_name = "partenaires"

urlpatterns = [
    # Clients
    path("clients/", views.client_list, name="client_list"),
    path("clients/nouveau/", views.client_create, name="client_create"),
    path("clients/<int:pk>/modifier/", views.client_update, name="client_update"),
    path("clients/<int:pk>/supprimer/", views.client_delete, name="client_delete"),
    # Fournisseurs
    path("fournisseurs/", views.fournisseur_list, name="fournisseur_list"),
    path("fournisseurs/nouveau/", views.fournisseur_create, name="fournisseur_create"),
    path(
        "fournisseurs/<int:pk>/modifier/",
        views.fournisseur_update,
        name="fournisseur_update",
    ),
    path(
        "fournisseurs/<int:pk>/supprimer/",
        views.fournisseur_delete,
        name="fournisseur_delete",
    ),
]
