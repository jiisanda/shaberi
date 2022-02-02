from django.urls import path
from userauth import views

urlpatterns = [
    path('login/', views.user_login_view, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.registrationView, name="register"),
]

