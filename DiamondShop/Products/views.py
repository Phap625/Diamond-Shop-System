from django.shortcuts import render
from Cart.models import Order
from .models import Category, Product

def category_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"

    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    else:
        products = Product.objects.none()

    sort_order = request.GET.get('sort', 'default')

    if products.exists():
        if sort_order == 'low_to_high':
            products = products.order_by('price')
        elif sort_order == 'high_to_low':
            products = products.order_by('-price')
        elif sort_order == 'best_seller':
            products = products.order_by('-sold')

    context = {
        'sort_order': sort_order,
        'collections':collections,
        'cart_items':cart_items,
        'categories':categories,
        'products':products ,
        'active_category':active_category,
        'user_not_login':user_not_login,
        'user_login':user_login
    }
    return render(request, 'Products/category.html', context)

def detail_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()

    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    categories = Category.objects.all()
    context = {
        'collections':collections,
        'cart_items': cart_items,
        'categories': categories,
        'products': products,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    return render(request, "Products/detail.html", context)

def collection_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection', flat=True).distinct()

    active_collection = request.GET.get('collection', '')

    products = Product.objects.filter(collection=active_collection) if active_collection else []
    sort_order = request.GET.get('sort', 'default')
    if sort_order == 'low_to_high':
        products = products.order_by('price')
    elif sort_order == 'high_to_low':
        products = products.order_by('-price')
    elif sort_order == "best_seller":
        products = products.order_by("-sold")
    categories = Category.objects.all()
    context = {
        'sort_order':sort_order,
        'collections': collections,
        'active_collection': active_collection,
        'cart_items': cart_items,
        'categories': categories,
        'products': products,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    return render(request, "Products/collection.html", context)