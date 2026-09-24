from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from projet_final.users.permissions import admin_role_required

from .forms import CommandeForm
from .forms import VenteForm
from .models import Commande
from .models import Vente
from .serializers import CommandeSerializer
from .serializers import VenteSerializer
from .services import StockInsuffisantError
from .services import creer_une_vente


# ---------- VENTES ----------
@login_required
def vente_list(request):
    ventes = Vente.objects.select_related("article", "client").all()
    return render(request, "transactions/vente_list.html", {"ventes": ventes})


@login_required
def vente_create(request):
    form = VenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Vente enregistrée avec succès.")
        return redirect("transactions:vente_list")
    return render(
        request,
        "transactions/vente_form.html",
        {"form": form, "titre": "Nouvelle vente"},
    )


@login_required
def vente_update(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    form = VenteForm(request.POST or None, instance=vente)
    if form.is_valid():
        form.save()
        messages.success(request, "ventes mise a jour ")
        return redirect("transactions:vente_list")
    return render(
        request,
        "transactions/vente_form.html",
        {"form": form, "titre": "Modifier vente"},
    )


@login_required
def vente_delete(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    if request.method == "POST":
        vente.delete()
        messages.success(request, "ventes suprimee")
        return redirect("transactions:vente_list")
    return render(
        request,
        "transactions/confirm_delete.html",
        {"objet": vente, "retour": "transactions:vente_list"},
    )


@admin_role_required
def vente_detail(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    return render(request, "transactions/vente_detail.html", {"vente": vente})


@login_required
def create_vente(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            try:
                vente = creer_une_vente(
                    article_id=form.cleaned_data["article"].id,
                    quantite_demandee=form.cleaned_data["quantite"],
                    client_id=form.cleaned_data["client"].id,
                )
                messages.success(request, f"Vente #{vente.pk} enregistrée avec succès.")
                return redirect("transactions:vente_list")
            except StockInsuffisantError as e:
                messages.error(request, str(e))
    else:
        form = VenteForm()
    return render(request, "transactions/vente_form.html", {"forms": form})


# ---------- COMMANDES ----------
@login_required
def commande_list(request):
    commandes = Commande.objects.select_related("article", "fournisseur").all()
    return render(request, "transactions/commande_list.html", {"commandes": commandes})


@login_required
def commande_create(request):
    form = CommandeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("transactions:commande_list")
    return render(
        request,
        "transactions/commande_form.html",
        {"form": form, "titre": "Nouvelle commande"},
    )


@login_required
def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)
    if form.is_valid():
        form.save()
        return redirect("transactions:commande_list")
    return render(
        request,
        "transactions/commande_form.html",
        {"form": form, "titre": "Modifier commande"},
    )


@login_required
def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == "POST":
        commande.delete()
        return redirect("transactions:commande_list")
    return render(
        request,
        "transactions/confirm_delete.html",
        {"objet": commande, "retour": "transactions:commande_list"},
    )


class VenteViewSet(ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer


class CommandeViewSet(ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
