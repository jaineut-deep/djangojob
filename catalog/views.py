from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from catalog.models import Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:pass_contacts")

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_details.html"
    context_object_name = "product"
