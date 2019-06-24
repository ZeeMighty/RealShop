
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from HiPage.models import Good
from . import forms

app_name = 'HiPage'
urlpatterns = [

    url(r'^$', views.IndexView, name = 'index'),
    url(r'men/', views.Men, name = 'men'),

    url(r'aboutus/', views.AboutUs, name = 'aboutus'),
    url(r'terms/', views.Terms, name = 'terms'),
    url(r'delivery/', views.Delivery, name = 'delivery'),
    url(r'return-policy/', views.Refund, name = 'refundpolicy'),
    url(r'support/', views.Support, name = 'support'),

    url(r'^add_to_cart/(?P<good_id>[0-9]+)/$', views.Adding.as_view(), name = 'adding_to_cart'),

    url(r'cart/', views.Cart, name = 'cart'),
]
