from django.shortcuts import render, redirect, get_object_or_404
from .models import Vente, Commande
from .forms import VenteForm, CommandeForm


# ---------- VENTES ----------

def vente_list(request):
    ventes = Vente.objects.select_related("article", "client").all()
    return render(request, "transactions/vente_list.html", {"ventes": ventes})


def vente_create(request):
    form = VenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("transactions:vente_list")
    return render(request, "transactions/vente_form.html", {"form": form, "titre": "Nouvelle vente"})


def vente_update(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    form = VenteForm(request.POST or None, instance=vente)
    if form.is_valid():
        form.save()
        return redirect("transactions:vente_list")
    return render(request, "transactions/vente_form.html", {"form": form, "titre": "Modifier vente"})


def vente_delete(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    if request.method == "POST":
        vente.delete()
        return redirect("transactions:vente_list")
    return render(request, "transactions/confirm_delete.html", {"objet": vente, "retour": "transactions:vente_list"})


# ---------- COMMANDES ----------

def commande_list(request):
    commandes = Commande.objects.select_related("article", "fournisseur").all()
    return render(request, "transactions/commande_list.html", {"commandes": commandes})


def commande_create(request):
    form = CommandeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("transactions:commande_list")
    return render(request, "transactions/commande_form.html", {"form": form, "titre": "Nouvelle commande"})


def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)
    if form.is_valid():
        form.save()
        return redirect("transactions:commande_list")
    return render(request, "transactions/commande_form.html", {"form": form, "titre": "Modifier commande"})


def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == "POST":
        commande.delete()
        return redirect("transactions:commande_list")
    return render(request, "transactions/confirm_delete.html", {"objet": commande, "retour": "transactions:commande_list"})
