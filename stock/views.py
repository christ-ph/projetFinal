from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.all()
    return render(request, "stock/article_list.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "stock/article_detail.html", {"article": article})


def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("stock:article_list")
    return render(request, "stock/article_form.html", {"form": form, "titre": "Nouvel article"})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect("stock:article_list")
    return render(request, "stock/article_form.html", {"form": form, "titre": "Modifier article"})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("stock:article_list")
    return render(request, "stock/confirm_delete.html", {"objet": article, "retour": "stock:article_list"})
