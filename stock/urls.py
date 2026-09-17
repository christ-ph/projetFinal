from django.urls import path
from .views import (
    ArticleList,
    ArticleDetail,
    ArticleCreate,
    ModifierArticle,
    SupprimerArticle,
)

app_name = "stock"

urlpatterns = [
    # path("", views.article_list, name="article_list"),
    path("", ArticleList.as_view(), name="article_list"),
    # path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    # path("nouveau/", views.article_create, name="article_create"),
    path("nouveau/", ArticleCreate.as_view(), name="article_create"),
    # path("<int:pk>/modifier/", views.article_update, name="article_update"),
    path("<int:pk>/modifier/", ModifierArticle.as_view(), name="article_update"),
    # path("<int:pk>/supprimer/", views.article_delete, name="article_delete"),
    path("<int:pk>/supprimer/", SupprimerArticle.as_view(), name="article_delete"),
]
