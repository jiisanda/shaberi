from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.urls import reverse

from userauth.forms import UserForm

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                print("LOGIN Failed !!!")
                print(f"User: {username} and password: {password}")
                messages.info(request,'invalid credentials')
                return redirect('user_login')            # here error possibility
    else:
        return render(request, 'userauth/login.html', {})


def registrationView(request):
    # if this is the POST request we need to process the form data
    template = 'userauth/registration.html'
    if request.method == "POST":
        # creating a form instance and populate it with data from the request: 
        form = UserForm(request.POST)
        # checking the form is valid
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form':form,
                    'error_message':'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form':form,
                    'error_message':'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form':form,
                    'error_message':'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to home page:
                return HttpResponseRedirect(reverse('home'))
    
    # No post data available, showing the same page
    else:
        form = UserForm()
    
    return render(request, template, {'form':form})



    #     profile_form = ProfileForm(data=request.POST)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         user.set_password(user.password)
    #         user.save()

    #         profile = profile_form.save(commit=False)
    #         if 'profile_picture' in request.FILES:
    #             profile.profile_picture = request.FILES['profile_picture']
    #         profile.save()
    #         registered = True
    #     else:
    #         print(user_form.errors, profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = ProfileForm()
    # return render(request, 'userauth/registration.html', {'user_form':user_form,'profile_form':profile_form, 'registered':registered})


# class ShowProfileView(DetailView):
#     model = UserProfileInfo
#     template_name='chats_app/base.html'
    
#     def get_context_data(self, *args, **kwargs):
#         user_section = UserProfileInfo.objects.all()
#         context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
#         context["user_section"] = user_section
#         return context