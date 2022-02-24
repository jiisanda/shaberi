from cProfile import label
from django.contrib.auth.models import User

from django import forms
from userauth.models import UserProfileInfo

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
    class Meta():
        model = UserProfileInfo
        fields = ()

        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-floating', 'placeholder':'Tell us who is writing Shaberi...'}),
            # 'phone_number':forms.CharField(widget=forms.NumberInput(attrs={'class':'form-floating'}), required=False),
        }

