from django.urls import path
from .views import (ContactsTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                    ProductDeleteView, CategoryDetailView)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="pass_home"),
    path("contacts/", ContactsTemplateView.as_view(), name="pass_contacts"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product_details/<int:pk>/", ProductDetailView.as_view(), name="pass_product_details"),
    path("category_details/<int:pk>/", CategoryDetailView.as_view(), name="pass_category_details"),
]
