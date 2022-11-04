from django.contrib import admin
from django.urls import path

from store.views.skinandhair import skinandhair
from .views.home import Index , store
from .views.signup import Signup
from .views.Otp import Otp
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.appointment import appointment
from .views.aboutus import aboutus
from .views.panchkarma import panchkarma
from .views.skinandhair import skinandhair
from .views.payment import payment
from .views.homepage import homepage
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage1'),
    path('store', store , name='store'),

    path('signup', Signup, name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('appointment', appointment ,name='appointment'),
    path('aboutus', aboutus ,name='aboutus'),
    path('panchkarma', panchkarma ,name='panchkarma'),
    path('skinandhair', skinandhair ,name='skinandhair'),
    path('payment', payment ,name='payment'),
    path('homepage', homepage ,name='homepage'),
    path('Otp', Otp.as_view() , name='Otp'),

]
