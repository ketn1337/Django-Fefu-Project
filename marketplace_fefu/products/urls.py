from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'products'

urlpatterns = [
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('category/<slug:category_slug>/details/<slug:product_slug>/', views.product, name='product'),
    path('', views.search, name="search"),
    path('buy/<slug:product_slug>', views.buy_product, name='buy_product'),
    path('buy/payment/success/', views.success, name='success'),
    path('buy/payment/failure/', views.failure, name='failure'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)