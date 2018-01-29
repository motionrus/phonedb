from django.conf.urls import url
from apps.phone import views


urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^table/$', views.customer_list, name='customer_list'),
    url(r'^table/create/$', views.customer_create, name='customer_create'),
    url(r'^table/(?P<pk>\d)/update/(?P<phone>\d+)$', views.customer_update, name='customer_update')
]
