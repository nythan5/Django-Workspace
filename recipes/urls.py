from django.urls import path
from recipes import views


urlpatterns = [
    path('outra-coisa-qualquer/', views.my_view),
    path('', views.home),  # Home
    path('sobre/', views.sobre),  # /sobre/
    path('contato/', views.contato),  # /contato/
]
