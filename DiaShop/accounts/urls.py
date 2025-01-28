from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_customer, name='register'),
    path('login/', views.login_customer, name='login'),
    path('profile/', views.profile_customer, name='profile'),
    path('logout/', views.logout_customer, name='logout'),
    path('update-info/', views.update_customer_info, name='update_info'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('enter-phone-number/', views.enter_phone_number, name='enter_phone_number'),

]
