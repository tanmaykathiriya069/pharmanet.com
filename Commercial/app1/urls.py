from os import name
from django.urls import path
from app1.views import *

urlpatterns = [
    path('',company_login,name='login'),
    path('register/',company_reg,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',company_logout,name='logout'),
    path('forgotpass/',forgot_pass,name='forgot'),
    path('newpass/',new_password,name='newpass'),
    path('otpcheck/',Otp_checker,name='otpcheck'),
    path('customer/',customer_page,name='customer'),
    path('delcustomer/<int:id>',delete_customer,name='deletecustomer'),
    path('delproduct/<int:id>',delete_product,name='deleteproduct'),
    path('updateproduct/<int:id>',update_product,name='updateproduct'),
    path('products/',product_page,name='products'),
    path('customerlogin/',customer_login,name='customerlogin'),
    path('error404/',error_404,name='error404'),
    path('error500/',error_500,name='error500'),
]
