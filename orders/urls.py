from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name="basket_adding"),
    url(r'^checkout/$', views.checkout, name="checkout"),
]
