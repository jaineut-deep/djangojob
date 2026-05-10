from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from catalog.models import Product
from .forms import ProductForm, ProductUserForm


class UnpublishProductMixin:
    redirect_url = "/"

    def post(self, request, *args, **kwargs):
        product = self.get_product()
        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав на изменение статуса публикации продукта")
        product.is_published = True if request.POST.get("is_published") == "on" else False
        return redirect(self.get_redirect_url(product))

    def get_product(self):
        if hasattr(self, "get_object"):
            try:
                return self.get_object()
            except AttributeError:
                pass
        return Product()

    def get_redirect_url(self, product):
        if product.pk:
            return reverse(self.redirect_url, kwargs={"pk": product.pk})
        return reverse(self.redirect_url)


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


class ProductCreateView(LoginRequiredMixin, UnpublishProductMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductUserForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:pass_home")
    redirect_url = "catalog:product_create"
    permission_required = "catalog.add_product"

    def post(self, request, *args, **kwargs):
        # super().post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = self.request.user
            product.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_details.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UnpublishProductMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    redirect_url = "catalog:product_update"

    def post(self, request, *args, **kwargs):
        # super().post(request, *args, **kwargs)
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = self.request.user
            product.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("catalog:pass_product_details", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name="Модератор продуктов").exists():
            return ProductForm
        if user == self.object.owner:
            return ProductUserForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:pass_home")
    permission_required = "catalog.delete_product"
