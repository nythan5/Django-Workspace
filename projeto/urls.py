
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('outra-coisa-qualquer/', views.my_view),
    path('', views.home),  # Home
    path('sobre/', views.sobre),  # /sobre/
    path('contato/', views.contato),  # /contato/
]
