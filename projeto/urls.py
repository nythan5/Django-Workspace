
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('About me')


urlpatterns = [

    # ele nunca começa com '/' mas pode terminar com /
    path('admin/', admin.site.urls),
    path('home/', my_view)

]
