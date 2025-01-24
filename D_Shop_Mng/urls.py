from django.urls import path
from . import views

urlpatterns = [
    path('D_Shop_Mng/', views.Product, name='Product'),
    path('D_Shop_Mng/', views.Collection, name='Collection'),
]