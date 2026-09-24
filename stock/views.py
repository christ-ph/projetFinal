from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from rest_framework.viewsets import ModelViewSet

from projet_final.users.permissions import AdminRoleRequiredMixin
from projet_final.users.permissions import CanManageArticles
from projet_final.users.permissions import StaffRoleRequiredMixin

from .forms import ArticleForm
from .models import Article
from .serializers import ArticleSerializer


class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    template_name = "stock/article_list.html"
    context_object_name = "articles"
    paginate_by = 18


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "stock/article_detail.html"
    context_object_name = "article"
    pk_url_kwarg = "pk"


class ArticleCreate(StaffRoleRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "stock/article_form.html"
    success_url = reverse_lazy("stock:article_list")

    def form_valid(self, form):
        messages.success(self.request, "Article enregistré avec succès.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titre"] = "Nouvel article"
        return context


class ModifierArticle(AdminRoleRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = (
        "stock/article_form.html"  # réutilise le même template que la création
    )
    success_url = reverse_lazy("stock:article_list")

    def form_valid(self, form):
        messages.success(self.request, "Article mis à jour avec succès.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titre"] = "Modifier l'article"
        return context


class SupprimerArticle(AdminRoleRequiredMixin, DeleteView):
    model = Article
    template_name = "stock/confirm_delete.html"
    context_object_name = "article"
    success_url = reverse_lazy("stock:article_list")

    def form_valid(self, form):
        messages.success(self.request, "Article supprimé avec succès.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        contexte["retour"] = "stock:article_list"
        contexte["nom"] = self.object.nom_article
        return contexte


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [CanManageArticles]
