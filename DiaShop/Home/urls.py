from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('detail/', views.detail_product, name='detail'),
    path('cart/', views.cart, name='cart')

]