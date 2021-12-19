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
    path('venueRegistration',views.venueregister,name='venueregister'),
    path('editVenue/<int:data>',views.editvenue,name='editvenue'),
    path('deleteVenue/<int:data>',views.deletevenue,name='deletevenue'),
    path('editVenue/venueUpdate',views.venueupdate,name='venueupdate'),
    path('venueDisplay/<int:data>',views.venuedynamic,name='venuedynamic'),
    path('venueDisplay/eventBooking',views.eventbook,name='eventbook'),
    path('eventList/<int:data>',views.eventlist,name='eventlist'),
    path('contactHost/<int:data>',views.contact,name='contact')
]