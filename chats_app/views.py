import json
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.utils.safestring import mark_safe

from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'chats_app\home.html'

def index(request):
    return render(request, 'chats_app/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chats_app/room.html', {
        'room_name_json':mark_safe(json.dumps(room_name)),
        'username':mark_safe(json.dumps(request.user.username)),
    })
