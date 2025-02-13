from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html')
def detail_product(request):
    context= {}
    return render(request, 'Detail.html', context)
def cart(request):
    context= {}
    return render(request, 'cart.html', context)