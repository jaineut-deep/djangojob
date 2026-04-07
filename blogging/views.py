from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from blogging.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blogging/article_form.html"
    success_url = reverse_lazy("blogging:article_list")


class ArticleListView(ListView):
    model = Article
    template_name = "blogging/article_list.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blogging/article_details.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.view_count += 1
        article.save()
        return article


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blogging/article_form.html"
    success_url = reverse_lazy("blogging:article_list")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blogging/article_confirm_delete.html"
    success_url = reverse_lazy("blogging:article_list")
