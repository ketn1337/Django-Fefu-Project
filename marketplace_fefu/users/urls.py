from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

appname = "users"

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('login', views.cust_login, name='login'),
    path('logout', views.cust_logout, name='logout'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)