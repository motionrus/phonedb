from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test(request):
    html = 'hello world'
    return HttpResponse(html)