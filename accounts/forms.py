from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class RegistrationForm(UserCreationForm):

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'email']

class AuthenticationForm(forms.Form):

    email=forms.EmailField()
    password1 = forms.CharField()

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        try:
            user = User.objects.get(email=email)
           
            return email
            
        except User.DoesNotExist:
            
            raise forms.ValidationError("User with this Email does not exist.")
            
        except Exception as e:
            
            raise forms.ValidationError('Request failed, try again later.')
        