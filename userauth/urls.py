from django.urls import path
from userauth import views
from .views import ProfileEditView

app_name = 'userauth'

urlpatterns = [
    path('login/', views.user_login_view, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.registrationView, name="register"),
    path('edit-profile/', ProfileEditView.as_view(), name="edit_profile")
]

