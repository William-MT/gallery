from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def land(req):
    return render(req, 'landpage.html')


def home(req):
    return render(req, 'home.html')


def collections(req):
    return render(req, 'collections.html')


def about(req):
    return HttpResponse('Hey W...')
