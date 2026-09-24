# transactions/services.py
from django.db import transaction
from django.utils import timezone
from stock.models import Article
from .models import Vente


class StockInsuffisantError(Exception):
    pass


@transaction.atomic
def creer_une_vente(article_id, quantite_demandee, client_id):
    """
    Crée une vente et diminue le stock de l'article correspondant,
    de façon atomique (tout réussit, ou rien n'est appliqué).
    """
    article = Article.objects.select_for_update().get(pk=article_id)

    if article.quantite < quantite_demandee:
        raise StockInsuffisantError(
            f"Vente impossible : quantité insuffisante "
            f"(demandé: {quantite_demandee}, disponible: {article.quantite})"
        )

    article.quantite -= quantite_demandee
    article.save()

    vente = Vente.objects.create(
        article=article,
        client_id=client_id,
        quantite=quantite_demandee,
        date=timezone.now(),
    )
    return vente
