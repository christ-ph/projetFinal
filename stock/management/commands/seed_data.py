"""
Commande de peuplement de la base avec des données de test.

Usage :
    uv run python manage.py seed_data
    uv run python manage.py seed_data --clients 200 --articles 150 --ventes 500
    uv run python manage.py seed_data --flush   # supprime tout avant de recréer
"""

import random
from decimal import Decimal
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from stock.models import Article
from partenaires.models import Client, Fournisseur
from transactions.models import Vente, Commande

fake = Faker("fr_FR")   # données francophones


CATEGORIES = [
    "Médicament",
    "Consommable",
    "Matériel",
    "Hygiène",
    "Vaccin",
    "Divers",
]


class Command(BaseCommand):
    help = "Remplit la base avec des données de test (clients, fournisseurs, articles, ventes, commandes)."

    def add_arguments(self, parser):
        parser.add_argument("--clients", type=int, default=50, help="Nombre de clients à créer")
        parser.add_argument("--fournisseurs", type=int, default=20, help="Nombre de fournisseurs")
        parser.add_argument("--articles", type=int, default=80, help="Nombre d'articles")
        parser.add_argument("--ventes", type=int, default=150, help="Nombre de ventes")
        parser.add_argument("--commandes", type=int, default=80, help="Nombre de commandes")
        parser.add_argument("--flush", action="store_true", help="Supprime toutes les données avant")

    @transaction.atomic
    def handle(self, *args, **options):
        if options["flush"]:
            self.stdout.write(self.style.WARNING("Suppression des données existantes…"))
            Vente.objects.all().delete()
            Commande.objects.all().delete()
            Article.objects.all().delete()
            Client.objects.all().delete()
            Fournisseur.objects.all().delete()

        # ---------- PARTENAIRES ----------
        clients = self._create_clients(options["clients"])
        fournisseurs = self._create_fournisseurs(options["fournisseurs"])

        # ---------- ARTICLES ----------
        articles = self._create_articles(options["articles"])

        # ---------- TRANSACTIONS ----------
        self._create_ventes(options["ventes"], articles, clients)
        self._create_commandes(options["commandes"], articles, fournisseurs)

        self.stdout.write(self.style.SUCCESS("\n✅ Base peuplée avec succès !"))
        self.stdout.write(f"  Clients      : {Client.objects.count()}")
        self.stdout.write(f"  Fournisseurs : {Fournisseur.objects.count()}")
        self.stdout.write(f"  Articles     : {Article.objects.count()}")
        self.stdout.write(f"  Ventes       : {Vente.objects.count()}")
        self.stdout.write(f"  Commandes    : {Commande.objects.count()}")

    # ---------- Helpers ----------
    def _create_clients(self, n):
        self.stdout.write(f"Création de {n} clients…")
        clients = [
            Client(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                telephone=fake.phone_number()[:20],
                adresse=fake.address().replace("\n", ", ")[:255],
            )
            for _ in range(n)
        ]
        return Client.objects.bulk_create(clients)

    def _create_fournisseurs(self, n):
        self.stdout.write(f"Création de {n} fournisseurs…")
        fournisseurs = [
            Fournisseur(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                telephone=fake.phone_number()[:20],
                adresse=fake.address().replace("\n", ", ")[:255],
            )
            for _ in range(n)
        ]
        return Fournisseur.objects.bulk_create(fournisseurs)

    def _create_articles(self, n):
        self.stdout.write(f"Création de {n} articles…")
        articles = []
        for _ in range(n):
            date_fab = fake.date_between(start_date="-2y", end_date="today")
            date_exp = date_fab + timedelta(days=random.randint(180, 1095))
            articles.append(
                Article(
                    nom_article=fake.unique.word().capitalize() + " " + fake.unique.bothify(text="??-##"),
                    categorie=random.choice(CATEGORIES),
                    quantite=random.randint(0, 500),
                    prix_unitaire=Decimal(random.randint(100, 50_000)),
                    date_fabrication=date_fab,
                    date_expiration=date_exp,
                )
            )
        return Article.objects.bulk_create(articles)

    def _create_ventes(self, n, articles, clients):
        self.stdout.write(f"Création de {n} ventes…")
        ventes = []
        for _ in range(n):
            a = random.choice(articles)
            c = random.choice(clients)
            qte = random.randint(1, 20)
            prix = a.prix_unitaire
            ventes.append(
                Vente(
                    article=a,
                    client=c,
                    quantite=qte,
                    prix=prix,
                )
            )
        return Vente.objects.bulk_create(ventes)

    def _create_commandes(self, n, articles, fournisseurs):
        self.stdout.write(f"Création de {n} commandes…")
        commandes = []
        for _ in range(n):
            a = random.choice(articles)
            f = random.choice(fournisseurs)
            qte = random.randint(10, 200)
            prix = a.prix_unitaire * Decimal("0.8")   # prix d'achat ~ -20 %
            commandes.append(
                Commande(
                    article=a,
                    fournisseur=f,
                    quantite=qte,
                    prix=prix.quantize(Decimal("0.01")),
                )
            )
        return Commande.objects.bulk_create(commandes)
