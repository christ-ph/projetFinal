from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Client, Fournisseur
from .forms import ClientForm, FournisseurForm
from .serializers import ClientSerializer, FournisseurSerializer
from projet_final.users.permissions import IsBusinessAdmin, admin_role_required


# ---------- CLIENTS ----------
@admin_role_required
def client_list(request):
    clients = Client.objects.all()
    page_obj = Paginator(clients, 18).get_page(request.GET.get("page"))
    return render(
        request,
        "partenaires/client_list.html",
        {"clients": page_obj, "page_obj": page_obj, "is_paginated": page_obj.has_other_pages()},
    )

@admin_role_required
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Client enregistré avec succès.")
        return redirect("partenaires:client_list")
    return render(request, "partenaires/client_form.html", {"form": form, "titre": "Nouveau client"})

@admin_role_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, "Client mis à jour avec succès.")
        return redirect("partenaires:client_list")
    return render(request, "partenaires/client_form.html", {"form": form, "titre": "Modifier client"})

@admin_role_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        messages.success(request, "Client supprimé avec succès.")
        return redirect("partenaires:client_list")
    return render(request, "partenaires/confirm_delete.html", {"objet": client, "retour": "partenaires:client_list"})


# ---------- FOURNISSEURS ----------
@admin_role_required
def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    page_obj = Paginator(fournisseurs, 18).get_page(request.GET.get("page"))
    return render(
        request,
        "partenaires/fournisseur_list.html",
        {"fournisseurs": page_obj, "page_obj": page_obj, "is_paginated": page_obj.has_other_pages()},
    )

@admin_role_required
def fournisseur_create(request):
    form = FournisseurForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Fournisseur enregistré avec succès.")
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/fournisseur_form.html", {"form": form, "titre": "Nouveau fournisseur"})

@admin_role_required
def fournisseur_update(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    form = FournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        messages.success(request, "Fournisseur mis à jour avec succès.")
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/fournisseur_form.html", {"form": form, "titre": "Modifier fournisseur"})

@admin_role_required
def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == "POST":
        fournisseur.delete()
        messages.success(request, "Fournisseur supprimé avec succès.")
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/confirm_delete.html", {"objet": fournisseur, "retour": "partenaires:fournisseur_list"})



class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsBusinessAdmin]


class FournisseurViewSet(ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
    permission_classes = [IsBusinessAdmin]



