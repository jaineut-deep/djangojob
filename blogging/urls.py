from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "blogging"


urlpatterns = [
    path("blogs/list/", ArticleListView.as_view(), name="article_list"),
    path("blogs/create/", ArticleCreateView.as_view(), name="article_create"),
    path("blogs/details/<int:pk>/", ArticleDetailView.as_view(), name="article_details"),
    path("blogs/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("blogs/delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
]
