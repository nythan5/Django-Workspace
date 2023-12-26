from django.urls import path
from recipes import views


urlpatterns = [
    path('pages/', views.home),  # Home

]
