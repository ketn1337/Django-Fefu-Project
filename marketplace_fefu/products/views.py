
from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Product, Category

def index(request):
    return HttpResponse("<html><body>hello</body></html>")

   


