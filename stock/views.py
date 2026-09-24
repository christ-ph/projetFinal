from rest_framework.viewsets import ModelViewSet
# from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView ,CreateView,DeleteView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import ArticleSerializer
from projet_final.users.permissions import AdminRoleRequiredMixin, CanManageArticles, StaffRoleRequiredMixin



class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    template_name = "stock/article_list.html"
    context_object_name = 'articles'
    paginate_by = 18

# def article_list(request):
#     articles = Article.objects.all()
#     return render(request, "stock/article_list.html", {"articles": articles})

class ArticleDetail(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "stock/article_detail.html"
    context_object_name = 'article'
    pk_url_kwarg = 'pk'

# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, "stock/article_detail.html", {"article": article})

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
# def article_create(request):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("stock:article_list")
#     return render(request, "stock/article_form.html", {"form": form, "titre": "Nouvel article"})



class ModifierArticle(AdminRoleRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "stock/article_form.html"   # réutilise le même template que la création
    success_url = reverse_lazy("stock:article_list")

    def form_valid(self, form):
        messages.success(self.request, "Article mis à jour avec succès.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titre"] = "Modifier l’article"
        return context


# def article_update(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     form = ArticleForm(request.POST or None, instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect("stock:article_list")
#     return render(request, "stock/article_form.html", {"form": form, "titre": "Modifier article"})

class SupprimerArticle(AdminRoleRequiredMixin, DeleteView):
    model = Article
    template_name = "stock/confirm_delete.html"
    context_object_name = 'article'
    success_url = reverse_lazy("stock:article_list")

    def form_valid(self, form):
        messages.success(self.request, "Article supprimé avec succès.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        contexte['retour'] = 'stock:article_list'
        contexte['nom'] = self.object.nom_article
        return contexte

# def article_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == "POST":
#         article.delete()
#         return redirect("stock:article_list")
#     return render(request, "stock/confirm_delete.html", {"objet": article, "retour": "stock:article_list"})



class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [CanManageArticles]
