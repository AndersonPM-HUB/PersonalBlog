from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("HOLA MUNDO")

def about(request): 
    return HttpResponse("ABOUT")