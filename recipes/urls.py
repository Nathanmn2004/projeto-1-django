
from django.http import HttpResponse
from django.urls import path
from recipes.views import sobre,contato,my_view



urlpatterns = [
    path('sobre/' , sobre),
    path('', my_view),
    path('contato', contato),
]