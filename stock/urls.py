from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("nouveau/", views.article_create, name="article_create"),
    path("<int:pk>/modifier/", views.article_update, name="article_update"),
    path("<int:pk>/supprimer/", views.article_delete, name="article_delete"),
]
