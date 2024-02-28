from django.shortcuts import render,redirect
from .forms import RegistrationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from .serializers import UserSerializer

from .models import User
from django.contrib import messages

# Create your views here.

def register(request):

    if request.user.is_authenticated :
        return redirect('home-page')
    
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():

                form.save()
                # Authenticate the user
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(email=email, password=password)

                if user is not None:
                    login(request, user)
                    request.session['id']=user.id
                    return redirect("home-page")  
        else:
            form = RegistrationForm()

        context = {'form': form}
        return render(request, 'register.html', context)


def auth_user(request):

    if request.user.is_authenticated :
        return redirect('home-page')
    else: 
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
        
            if form.is_valid():
                email=form.cleaned_data.get('email')
                password=form.cleaned_data.get('password1')
                
                try:
                    user = authenticate(email=email, password=password)
                    
                    if user is not None:  

                        login(request,user)
                        return redirect('home-page')  
                    else:
                        messages.error(request,"Invalid email or password.")
                except Exception as e:
                    messages.error(request,e)       
            else:
                print(form.errors)            
        else:
            form = AuthenticationForm()

        context = {'form': form}
        return render(request, 'login.html', context)


def index(request):
    return render(request,'index.html')