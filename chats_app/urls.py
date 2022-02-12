from django.urls import path

from chats_app.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('chat/', views.index, name="index"),
    path('chat/<str:room_name>/', views.room, name='room'),
]
