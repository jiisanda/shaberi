from django.contrib.auth.models import User

from django import forms
from userauth.models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_repeat', 'phone_number')


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'phone_number','profile_picture')
