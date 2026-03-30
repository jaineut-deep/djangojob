from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


def pass_home(request):
    return render(request, 'catalog/home.html')


def pass_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')


def pass_product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, "catalog/product_details.html", context)

