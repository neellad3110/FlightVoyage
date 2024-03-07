from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    """"
        Form for user authentication.

        Validates email input and checks if a user with the provided email exists in the database.
    """

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'email']

class AuthenticationForm(forms.Form):
    """
        Form for user authentication.

        Validates email input and checks if a user with the provided email exists in the database.
    """

    email=forms.EmailField()
    password1 = forms.CharField()

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        try:
            User.objects.get(email=email)
           
            return email
            
        except User.DoesNotExist:
            
            raise forms.ValidationError("User with this Email does not exist.")
            
        except Exception as e:
            
            raise forms.ValidationError('Request failed, try again later.')
        