from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Image
import random
# Create your views here.


def land(req):
    return render(req, 'landpage.html')


def home(req):
    vimgs = list(Image.objects.all().values())
    random.shuffle(vimgs)
    template = loader.get_template('home.html')
    vi = ['earth.jpg','spectrum.jpg', 'darkcloud.jpg', 'eggs.jpg', 'icemountian.jpg', 'gosh.png', 'lionking.png']
    vcontext = {
        'imgs': vimgs,
        'cat': [0, 1, 2],
        'img': vi,

    }
    return HttpResponse(template.render(vcontext, req))


def collections(req):
    return render(req, 'collections.html')


def about(req):
    return HttpResponse('Hey W...')
