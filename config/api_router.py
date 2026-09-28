# config/api_router.py
from rest_framework.routers import DefaultRouter

from partenaires.views import ClientViewSet
from partenaires.views import FournisseurViewSet
from stock.views import ArticleViewSet
from transactions.views import CommandeViewSet
from transactions.views import VenteViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet)
router.register("clients", ClientViewSet)
router.register("fournisseurs", FournisseurViewSet)
router.register("ventes", VenteViewSet)
router.register("commandes", CommandeViewSet)

urlpatterns = router.urls
