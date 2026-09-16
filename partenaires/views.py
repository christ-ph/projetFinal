from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Fournisseur
from .forms import ClientForm, FournisseurForm


# ---------- CLIENTS ----------

def client_list(request):
    clients = Client.objects.all()
    return render(request, "partenaires/client_list.html", {"clients": clients})


def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("partenaires:client_list")
    return render(request, "partenaires/client_form.html", {"form": form, "titre": "Nouveau client"})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect("partenaires:client_list")
    return render(request, "partenaires/client_form.html", {"form": form, "titre": "Modifier client"})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("partenaires:client_list")
    return render(request, "partenaires/confirm_delete.html", {"objet": client, "retour": "partenaires:client_list"})


# ---------- FOURNISSEURS ----------

def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, "partenaires/fournisseur_list.html", {"fournisseurs": fournisseurs})


def fournisseur_create(request):
    form = FournisseurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/fournisseur_form.html", {"form": form, "titre": "Nouveau fournisseur"})


def fournisseur_update(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    form = FournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/fournisseur_form.html", {"form": form, "titre": "Modifier fournisseur"})


def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == "POST":
        fournisseur.delete()
        return redirect("partenaires:fournisseur_list")
    return render(request, "partenaires/confirm_delete.html", {"objet": fournisseur, "retour": "partenaires:fournisseur_list"})
