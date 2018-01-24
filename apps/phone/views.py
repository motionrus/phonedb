from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from apps.phone.models import Customer
# Create your views here.


def test(request):
    html = 'hello world'
    return HttpResponse(html)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'table.html', {'customers': customers})

'''
class TableView(View):
    template_name = "includes/table.html"

    def get(self, request):
        list_customer = Customer.objects.all()
        return HttpResponse(list_customer)
'''