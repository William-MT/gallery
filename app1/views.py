from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Image
import random
# Create your views here.

oimgs = ['earth.jpg','spectrum.jpg', 'darkcloud.jpg', 'eggs.jpg', 'icemountian.jpg', 'gosh.png', 'lionking.png',
    'spicies.jpg', 'eggs.jpg']


def land(req):
    vimgs = list(Image.objects.all().values())
    random.shuffle(vimgs)
    template = loader.get_template('landpage.html')

    context = {
        'oimgs': oimgs,
        'imgs': vimgs,
        'cat': [0, 1, 2],
    }
    return HttpResponse(template.render(context, req))



def home(req):
    vimgs = list(Image.objects.all().values())
    random.shuffle(vimgs)
    template = loader.get_template('home.html')
    vcontext = {
        'oimgs': oimgs,
        'imgs': vimgs,
        'cat': [0, 1, 2],

    }
    return HttpResponse(template.render(vcontext, req))


def collections(req):
    vimgs = list(Image.objects.all().values())
    random.shuffle(vimgs)
    template = loader.get_template('collections.html')
    context = {
        'oimgs': oimgs,
        'oimg0': oimgs[0],
        'oimg1': oimgs[1],
        'oimg2': oimgs[2],
        'imgs': vimgs,
        'nimgs': list(range(len(vimgs))),
        'cat': [0, 1, 2],
    }
    return HttpResponse(template.render(context, req))



def about(req):
    template = loader.get_template('about.html')
    context = {
    }
    return HttpResponse(template.render(context, req))

