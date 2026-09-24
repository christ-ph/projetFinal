from django.urls import path

from .views import ArticleCreate
from .views import ArticleDetail
from .views import ArticleList
from .views import ModifierArticle
from .views import SupprimerArticle

app_name = "stock"

urlpatterns = [
    path("", ArticleList.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    path("nouveau/", ArticleCreate.as_view(), name="article_create"),
    path("<int:pk>/modifier/", ModifierArticle.as_view(), name="article_update"),
    path("<int:pk>/supprimer/", SupprimerArticle.as_view(), name="article_delete"),
]
