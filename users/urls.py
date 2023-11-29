from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('login', views.cust_login, name='login'),
    path('logout', views.cust_logout, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    path('profle/<username>/create_product', views.create_product, name='create_product'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)