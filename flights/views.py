from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from accounts.serializers import UserSerializer

# Create your views here.
@login_required(login_url='/accounts/login')
def flights(request):
    if request.user.is_authenticated :
       serialized_data=UserSerializer(request.user);
       return render(request,'flights.html', {'response': serialized_data.data})  

def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('index-page')
