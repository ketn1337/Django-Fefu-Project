
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category
from django.db.models import Q

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'product/category.html', {'category': category})


def product(request, category_slug, product_slug):
    pass


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    categories = Category.objects.all()
    context = {'products': products, 'query': query, 'categories': categories}

    return render(request, 'products/search.html', context)

   


