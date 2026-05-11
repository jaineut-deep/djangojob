from config.settings import CACHE_ENABLED
from django.core.cache import cache
from .models import Product


class CategoryService:

    @staticmethod
    def get_category_products(category_id):
        if not CACHE_ENABLED:
            return Product.objects.filter(category_id=category_id)
        key = f"category_products_{category_id}"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60 * 15)
        return products
