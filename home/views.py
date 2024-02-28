from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from accounts.serializers import UserSerializer

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    if request.user.is_authenticated :
       serialized_data=UserSerializer(request.user);
       return render(request,'home.html', {'response': serialized_data.data})  

@login_required(login_url='/accounts/login')
def mybookings(request):
      return render(request,'bookings.html')
      


def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('index-page')
