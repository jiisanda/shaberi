from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'chats_app\home.html'

def index(request):
    return render(request, 'chats_app/index.html')

def room(request, room_name):
    return render(request, 'chats_app/room.html', {
        'room_name':room_name,
    })
