from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "nom_article",
        "categorie",
        "quantite",
        "prix_unitaire",
        "date_fabrication",
        "date_expiration",
        "en_stock",
    )
    search_fields = ("nom_article", "categorie")
    list_filter = ("categorie", "date_expiration", "date_fabrication")
    ordering = ("nom_article",)
    list_per_page = 25
    date_hierarchy = "date_fabrication"   # barre de navigation par date en haut

    fieldsets = (
        ("Article", {
            "fields": ("nom_article", "categorie")
        }),
        ("Stock et prix", {
            "fields": ("quantite", "prix_unitaire")
        }),
        ("Dates", {
            "fields": ("date_fabrication", "date_expiration")
        }),
    )

    @admin.display(description="En stock", boolean=True)
    def en_stock(self, obj):
        return obj.quantite > 0
