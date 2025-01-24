from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def Product(request):
    return HttpResponse("Hello world!")

def Collection(request):
    return HttpResponse("Hello world!")