from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name='index-page'),
    path('accounts/register/',views.register, name='register-page'),
    path('accounts/login/',views.auth_user, name='login-page'),   
]