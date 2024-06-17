from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')

def my_view(request):
    return HttpResponse('HOME')