from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    context = {}
    template = loader.get_template('agreementGen/index.html')
    return HttpResponse(template.render(context, request))

def signup(request):
    context = {}
    template = loader.get_template('agreementGen/signup.html')
    return HttpResponse(template.render(context, request))
