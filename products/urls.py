from django.conf.urls import url
from products import views

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name="product"),
]
