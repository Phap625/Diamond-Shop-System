from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderDetail
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def order_list(request):
    orders = Order.objects.filter(Customer=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


# Create your views here.
