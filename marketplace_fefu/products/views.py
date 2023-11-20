
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import User
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
    products = Product.objects.all()
    categories = Category.objects.all()
    category_slug = request.GET.get('category', 0)
    if query:
        products = products.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category = category)

    context = {'products': products, 'query': query, 'categories': categories}

    return render(request, 'products/search.html', context)


@login_required
def buy_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    user = request.user
    vendor = product.vendor
    if user.balance >= product.price:
        user.balance -= product.price
        user.save()
        vendor.balance += product.price
        vendor.save()
        product.delete()
        return redirect('payment/success/')
    
    return redirect('payment/failure/')


def success(request):
    return render(request, 'products/success.html')


def failure(request):
    return render(request, 'products/failure.html')