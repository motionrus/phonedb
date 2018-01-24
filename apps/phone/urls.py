from django.conf.urls import url
from apps.phone import views

from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^table/', views.customer_list, name='customer_list'),
]
