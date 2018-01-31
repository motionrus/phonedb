from django.shortcuts import render
from django.http import HttpResponse
from apps.phone.models import Customer, Number
from apps.phone.forms import CustomerForm, NumberForm, CreateNumberForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.


def test(request):
    html = 'hello world'
    return HttpResponse(html)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'includes/table.html', {'customers': customers})


def save_customer(request, form_customer, form_number, template_name):
    data = dict()
    if request.method == 'POST':
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
    context = {'form_customer': form_customer, 'form_number': form_number}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def customer_create(request):
    if request.method == 'POST':
        form_customer = CustomerForm(request.POST)
        form_number = NumberForm(request.POST)
    else:
        form_customer = CustomerForm()
        form_number = NumberForm()
    return save_customer(request, form_customer, form_number, 'includes/customer_create.html')


def customer_update(request, pk, phone):
    customer = get_object_or_404(Customer, pk=int(pk))
    number = get_object_or_404(Number, internal_number=phone)
    if request.method == 'POST':
        form_customer = CustomerForm(request.POST, instance=customer)
        form_number = NumberForm(request.POST, instance=number)
    else:
        form_customer = CustomerForm(instance=customer)
        form_number = NumberForm(instance=number)
    return save_customer(request, form_customer, form_number, 'includes/customer_update.html')


def number_create(request, pk, phone):
    data = dict()
    customer = get_object_or_404(Customer, pk=pk)
    form_number = CreateNumberForm()
    form_number.customer = customer
    if request.method == 'POST':
        form_number = CreateNumberForm(request.POST)
        if form_number.is_valid():
            post_form_number = form_number.save(commit=False)
            post_form_number.customer = customer
            post_form_number.save()
            data['form_is_valid'] = True
            data['html_customer_list'] = render_to_string('includes/part_list.html', {
                'customers': Customer.objects.all()})
        else:
            data['form_is_valid'] = False
    context = {'form_number': form_number, 'pk': pk, 'phone': phone}
    data['html_form'] = render_to_string('includes/number_create.html', context, request=request)
    return JsonResponse(data)


def customer_delete(request, phone):
    phone = get_object_or_404(Number, internal_number=phone)
    data = dict()
    if request.method == 'POST':
        phone.delete()
        data['form_is_valid'] = True
        data['html_customer_list'] = render_to_string('includes/part_list.html', {
            'customers': Customer.objects.all()
        })
    else:
        context = {'phone': phone}
        data['html_form'] = render_to_string('includes/number_delete.html', context, request=request)
    return JsonResponse(data)
