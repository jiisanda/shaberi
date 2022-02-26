from cProfile import label
from attr import field
from django.contrib.auth.models import User

from django import forms
from userauth.models import UserProfileInfo

from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), label=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name*'}), label=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name*'}), label=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username*'}), label=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}), label=False)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Tell us who is writing Shaberi...', 'rows':"2"}), label=False)
    phone_number = PhoneNumberField()
    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'phone_number', 'profile_picture')


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name*'}), label=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name*'}), label=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username*'}), label=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}), label=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Tell us who is writing Shaberi...', 'rows':"2"}), label=False)
    phone_number = PhoneNumberField()

    class Meta():
        model = UserProfileInfo
        fields = ('first_name', 'last_name', 'username', 'email', 'bio', 'phone_number', 'profile_picture')
