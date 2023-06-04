from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket


def index(request):
    context = {'title': 'Store Yo',
               'is_promotion': True}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Store - products',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()
               }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.created(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
