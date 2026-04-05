from django.urls import path
from .views import ContactsTemplateView, ProductListView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="pass_home"),
    path("contacts/", ContactsTemplateView.as_view(), name="pass_contacts"),
    path("product_details/<int:pk>/", ProductDetailView.as_view(), name="pass_product_details"),
]
