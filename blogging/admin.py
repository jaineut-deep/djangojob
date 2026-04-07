from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "view_count")
    list_filter = ("created_at",)
    search_fields = ("title",)
