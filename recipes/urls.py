
from django.http import HttpResponse
from django.urls import path
from recipes.views import sobre,contato,home



urlpatterns = [
    path('sobre/' , sobre),
    path('', home),
    path('contato', contato),
]