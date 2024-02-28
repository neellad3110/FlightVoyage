from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name='home-page'),
    path('mybookings/',views.mybookings,name='mybookings-page'),
    path('logout/',views.userlogout, name='logout-page'),   

]