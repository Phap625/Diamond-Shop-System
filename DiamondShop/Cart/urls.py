from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_view, name='cart'),
    path("checkout/", views.checkout_view, name='checkout'),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
]