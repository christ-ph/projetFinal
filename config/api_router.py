from django.conf import settings
# config/api_router.py
from rest_framework.routers import DefaultRouter

from stock.views import ArticleViewSet
from partenaires.views import ClientViewSet, FournisseurViewSet
from transactions.views import VenteViewSet, CommandeViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('clients', ClientViewSet)
router.register('fournisseurs', FournisseurViewSet)
router.register('ventes', VenteViewSet)
router.register('commandes', CommandeViewSet)

urlpatterns = router.urls
