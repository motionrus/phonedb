from django.shortcuts import render
from django.http import HttpResponse
from apps.phone.models import Customer
from apps.phone.forms import PhoneForm
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.


def test(request):
    html = 'hello world'
    return HttpResponse(html)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'table.html', {'customers': customers})


def customer_create(request):
    data = dict()
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True

        else:
            data['form_is_valid'] = False

    else:
        form = PhoneForm()

    context = {'form': form}
    html_form = render_to_string('includes/create_customer.html',
                                 context,
                                 request=request,
                                 )
    return JsonResponse({'html_form': html_form})
