from django.shortcuts import render
from django.http import HttpResponse
from apps.phone.models import Customer
from apps.phone.forms import CustomerForm, NumberForm
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.


def test(request):
    html = 'hello world'
    return HttpResponse(html)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'includes/table.html', {'customers': customers})


def customer_create(request):
    data = dict()
    if request.method == 'POST':
        form_customer = CustomerForm(request.POST)
        form_number = NumberForm(request.POST)
        if form_customer.is_valid() and form_number.is_valid():
            form_customer.save()
            post_form_number = form_number.save(commit=False)
            post_form_number.customer = Customer.objects.get(name=request.POST['name'])
            post_form_number.save()
            data['form_is_valid'] = True
            customers = Customer.objects.all()
            data['html_customer_list'] = render_to_string('includes/part_list.html', {
                'customers': customers
            })
        else:
            data['form_is_valid'] = False
    else:
        form_customer = CustomerForm()
        form_number = NumberForm()

    context = {'form': form_customer, 'form2': form_number}
    data['html_form'] = render_to_string('includes/create_customer.html',
                                 context,
                                 request=request,
                                 )
    return JsonResponse(data)


