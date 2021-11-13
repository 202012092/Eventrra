from django.urls import path

from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('eventHostRegister',views.ehregister,name='ehregister'),
    path('venueHolderRegister',views.vhregister,name='vhregister'),
    path('eventHostRegisteration',views.ehaccount,name='ehaccount'),
    path('venueHolderRegisteration',views.vhaccount,name='vhaccount'),
    path('eventHostLogin',views.ehlogin,name='ehlogin'),
    path('venueHolderLogin',views.vhlogin,name='vhlogin'),
    path('ehLogout',views.ehlogout,name='ehlogout'),
    path('vhLogout',views.vhlogout,name='vhlogout'),
    path('addVenue',views.addvenue,name='addvenue'),
    path('venueRegistration',views.venueregister,name='venueregister')
]