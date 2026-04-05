from django.urls import path
from . import views


app_name = "catalog"

urlpatterns = [
    path("", views.pass_home, name="pass_home"),
    path("contacts/", views.pass_contacts, name="pass_contacts"),
    path("product_details/<int:pk>/", views.pass_product_details, name="pass_product_details"),
]