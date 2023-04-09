from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def land(req):
    return render(req, 'landpage.html')


def home(req):
    return HttpResponse('Hey W...')
