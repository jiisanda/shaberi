from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import UpdateView

from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from userauth.forms import UserForm, ProfileForm, ProfileEditForm

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('chats_app:home'))


def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('chats_app:home')) 
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to logon and failed...")
            print(f"User: {username} and password {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'userauth/login.html', {})


def registrationView(request):
    registered = False
    # if this is the POST request we need to process the form data
    if request.method == "POST":
        # creating a form instance and populate it with data from the request: 
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        # checking the form is valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'userauth/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})
            
class ProfileEditView(UpdateView):
    form_class = ProfileEditForm
    template_name = 'userauth/edit_profile.html'
    success_url = reverse_lazy('chats_app:home')

    def get_object(self):
        return self.request.user
    
