from django.urls import path
from userauth import views
from userauth.views import ChangePasswordView

app_name = 'userauth'

urlpatterns = [
    path('login/', views.user_login_view, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.registrationView, name="register"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('password-change/', ChangePasswordView.as_view(), name="edit_password"),
]

