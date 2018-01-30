from django.conf.urls import url
from apps.phone import views


urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^customer/$', views.customer_list, name='customer_list'),
    url(r'^customer/create/$', views.customer_create, name='customer_create'),
    url(r'^customer/(?P<pk>\d+)/update/(?P<phone>\d+)$', views.customer_update, name='customer_update'),
    url(r'^customer/delete/(?P<phone>\d+)$', views.customer_delete, name='customer_delete'),
    url(r'^customer/(?P<pk>\d+)/add_number/(?P<phone>\d+)$', views.number_create, name='number_create')
]
