from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. I am GREEN ROBOT ")
# Create your views here.
