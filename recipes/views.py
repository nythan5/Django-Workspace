from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    return HttpResponse('UM LINDA STRING')


def home(request):
    return HttpResponse('HOME')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
