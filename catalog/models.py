from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="Наименование")
    description = models.CharField(max_length=150, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name="Наименование")
    description = models.CharField(max_length=150, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products",
                                 verbose_name="Категория")
    purchase_price = models.FloatField(verbose_name="Цена за покупку")
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return f"{self.name} - {self.category}"

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.owner:
                raise ValueError("Владелец должен быть передан")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
