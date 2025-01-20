from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_customer, name='register'),
    path('login/', views.login_customer, name='login'),
]
