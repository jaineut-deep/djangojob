from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="images/", verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title} / {self.created_at}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]
