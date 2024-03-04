from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.flights, name='flight-page'),
    path('bookflight/',views.bookflight,name='flight-booking-page'),
   
]