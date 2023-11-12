from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('<slug:category_slug>/', views.category, name='category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('', views.search, name="search"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)