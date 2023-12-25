from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    return HttpResponse('UM LINDA STRING')


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Gabriel Nathan'},)


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('sobre')
