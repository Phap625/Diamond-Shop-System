from django.shortcuts import render
from .models import *
from Products.models import Product, Category
from django.http import JsonResponse
import json

def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    context = {'collections':collections, 'categories':categories,'items': items, 'order': order, 'cart_items': cart_items, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'Cart/cart.html', context)


def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    context = {'collections':collections, 'categories':categories, 'items':items, 'order':order, 'cart_items':cart_items, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'Cart/checkout.html', context)

def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("productId")
        action = data.get("action")
        customer = request.user
        product = Product.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == "add":
            order_item.quantity += 1
        elif action == "remove":
            order_item.quantity -= 1
        order_item.save()
        if order_item.quantity <= 0:
            order_item.delete()

        return JsonResponse({"message": "Cập nhật giỏ hàng thành công", "quantity": order_item.quantity}, safe=False)