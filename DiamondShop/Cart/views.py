from django.shortcuts import render
from .models import *
from Products.models import Product, Category
from django.http import JsonResponse
import json

def cart_view(request):
    purchased_items = []
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        completed_orders = Order.objects.filter(customer=customer, complete=True).order_by("-id")
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
        for completed_order in completed_orders:
            purchased_items.extend(completed_order.orderitem_set.all())
            shopping_address = ShoppingAddress.objects.filter(order=completed_order).first()
            if shopping_address:
                for item in purchased_items:
                    item.created_at = shopping_address.created_at
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    context = {
        'purchased_items': purchased_items,
        'collections':collections,
        'categories':categories,
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'user_not_login':user_not_login,
        'user_login':user_login
    }
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
    context = {
        "confirm": "show",
        "thank_you": "hidden",
        'collections':collections,
        'categories':categories,
        'items':items, 'order':order,
        'cart_items':cart_items,
        'user_not_login':user_not_login,
        'user_login':user_login
    }
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


def shopping_address(request):
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"

        if request.method == "POST":
            name_order = request.POST.get("name")
            phone_number = request.POST.get("phone_number")
            note = request.POST.get("note")
            city = request.POST.get("city")
            district = request.POST.get("district")
            commune = request.POST.get("commune")
            address_detail = request.POST.get("address")

            full_address = f"{city}, {district}, {commune}, {address_detail}"
            order = Order.objects.filter(customer=request.user, complete=False).first()
            if not note:
                note = "Không có ghi chú"

            if order:
                ShoppingAddress.objects.create(
                    customer=request.user,
                    name_order=name_order,
                    order=order,
                    address=full_address,
                    phone_number=phone_number,
                    note=note
                )
                order.complete = True
                order.save()
                cart_items = 0
            context = {
                "confirm": "hidden",
                "thank_you": "show",
                "name_order": name_order,
                "phone_number": phone_number,
                "note": note,
                "city": city,
                "district": district,
                "commune": commune,
                "address_detail": address_detail,
                'collections': collections,
                'categories': categories,
                'items': items,
                'order': order,
                'cart_items': cart_items,
                'user_not_login': user_not_login,
                'user_login': user_login
            }
            return render(request, "Cart/checkout.html", context)
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"

    context = {
        "confirm": "show",
        "thank_you": "hidden",
        'collections': collections,
        'categories': categories,
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'user_not_login': user_not_login,
        'user_login': user_login
    }

    return render(request, "Cart/checkout.html", context)