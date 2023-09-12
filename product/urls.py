from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('allitems',views.allitems,name='allitems'),
    path('surf',views.surf,name='surf'),
    path('search',views.search,name='search'),
    path('mycart',views.mycart,name='mycart'),
    path('payment',views.make_payment,name='payment'),
]