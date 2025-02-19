from django.shortcuts import render
from Products.models import Product, Category
from Cart.models import Order


def home_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        cart_items = 0
        user_login = "hidden"
        user_not_login = "show"

    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                              flat=True).distinct()
    categories = Category.objects.all()

    sort_order = request.GET.get('sort', 'default')
    if sort_order == 'low_to_high':
        products = Product.objects.all().order_by('price')
    elif sort_order == 'high_to_low':
        products = Product.objects.all().order_by('-price')
    elif sort_order == "best_seller":
        products = Product.objects.all().order_by("-sold")
    else:
        products = Product.objects.all()

    context = {
        'collections':collections,
        'categories':categories,
        'products':products,
        'cart_items':cart_items,
        'user_not_login':user_not_login,
        'user_login':user_login,
        'sort_order': sort_order
    }
    return render(request, "Home/home.html", context)


def search_view(request):
    keys = Product.objects.none()
    searched = request.GET.get("searched", "").strip()
    if searched:
        keys = Product.objects.filter(name__icontains=searched)

    if request.method == "POST":
        searched = request.POST.get("searched", "").strip()
        if searched:
            keys = Product.objects.filter(name__icontains=searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        cart_items = 0
        user_not_login = "show"
        user_login = "hidden"
    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()

    sort_order = request.GET.get('sort', 'default')

    if sort_order == 'low_to_high':
        keys = keys.order_by('price')
    elif sort_order == 'high_to_low':
        keys = keys.order_by('-price')
    elif sort_order == "best_seller":
        keys = keys.order_by("-sold")
    context = {
        'sort_order': sort_order,
        'collections': collections,
        'categories':categories,
        'searched':searched,
        'keys':keys,
        'cart_items':cart_items,
        'user_not_login':user_not_login,
        'user_login':user_login,
    }
    return render(request, "Home/search.html",context)

def contact_view(request):
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
        user_login = "hidden"
        user_not_login = "show"

    collections = Product.objects.exclude(collection__isnull=True).exclude(collection="").values_list('collection',
                                                                                                      flat=True).distinct()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'collections':collections,
        'categories':categories,
        'products':products,
        'cart_items':cart_items,
        'user_not_login':user_not_login,
        'user_login':user_login
    }
    return render(request, 'Home/contact.html', context)