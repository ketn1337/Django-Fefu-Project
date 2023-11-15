
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category
from django.db.models import Q

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = {'category': category}
    return render(request, 'products/category.html', context)


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    categories = Category.objects.all()
    context = {'products': products, 'query': query, 'categories': categories}

    return render(request, 'products/search.html', context)




