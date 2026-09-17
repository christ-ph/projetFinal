# from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView ,CreateView,DeleteView,DetailView,UpdateView



class ArticleList(ListView):
    model = Article
    template_name = "stock/article_list.html"
    context_object_name = 'articles'

# def article_list(request):
#     articles = Article.objects.all()
#     return render(request, "stock/article_list.html", {"articles": articles})

class ArticleDetail(DetailView):
    model = Article
    template_name = "stock/article_detail.html"
    context_object_name = 'article'
    pk_url_kwarg = 'pk'

# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, "stock/article_detail.html", {"article": article})

class ArticleCreate(CreateView):
        model = Article
        form_class = ArticleForm
        template_name = "stock/article_form.html"
        success_url = reverse_lazy("stock:article_list")
# def article_create(request):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("stock:article_list")
#     return render(request, "stock/article_form.html", {"form": form, "titre": "Nouvel article"})



class ModifierArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "stock/article_form.html"   # réutilise le même template que la création
    success_url = reverse_lazy("stock:article_list")


# def article_update(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     form = ArticleForm(request.POST or None, instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect("stock:article_list")
#     return render(request, "stock/article_form.html", {"form": form, "titre": "Modifier article"})

class SupprimerArticle(DeleteView):
    model = Article
    template_name = "stock/confirm_delete.html"
    context_object_name = 'article'
    success_url = reverse_lazy("stock:article_list")

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
