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
        form = CustomerForm(request.POST)
        form2 = NumberForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            my_model = form2.save(commit=False)
            my_model.customer = Customer.objects.get(request.POST['name'])
            form2.save()
            data['form_is_valid'] = True
            customers = Customer.objects.all()
            data['html_customer_list'] = render_to_string('includes/part_list.html', {
                'customers': customers
            })
        else:
            data['form_is_valid'] = False
    else:
        form = CustomerForm()
        form2 = NumberForm()

    context = {'form': form, 'form2': form2}
    data['html_form'] = render_to_string('includes/create_customer.html',
                                 context,
                                 request=request,
                                 )
    return JsonResponse(data)


