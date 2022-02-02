from django import forms
from django.contrib.auth.models import User
from userauth.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio', 'phone_number','profile_picture')
