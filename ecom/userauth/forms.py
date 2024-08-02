# from django.contrib.auth.forms import UserCreationForm
# from userauth.models import User

# class Userregistrationform(UserCreationForm):

#     class meta:
#         model=User
#         fields=['username','email']

from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class userloginform(AuthenticationForm):
    #  email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
     username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
     password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
     class meta:
         model=User
         fields=('email')
