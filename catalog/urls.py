from django.urls import path
from . import views


urlpatterns = [
    path("", views.pass_home, name="pass_home"),
    path("contacts/", views.pass_contacts, name="pass_contacts")
]