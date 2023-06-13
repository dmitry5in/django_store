from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {'title': 'Store Yo',
               'is_promotion': True}
    return render(request, 'products/index.html', context)


def products(request, category_id=0, page_number=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(product, 3)
    product_paginator = paginator.page(page_number)
    context = {'title': 'Store - products',
               'products': product_paginator,
               'categories': ProductCategory.objects.all(),
               'select_cat': category_id
               }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
