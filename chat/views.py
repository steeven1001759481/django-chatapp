from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def checkView(request):
    roomName = request.POST['room_name']
    userName = request.POST['user_name']
    if Room.objects.filter(name=roomName).exists():
        return redirect('chat/'+roomName+'/?user_name='+userName)
    else:
        newRoom = Room.objects.create(name=roomName)
        newRoom.save()
        return redirect('chat/'+roomName+'/?user_name='+userName)

def roomView(request,room):
    userName = request.GET.get('user_name')
    roomName = Room.objects.get(name=room)
    context = {
        'room': roomName,
        'user': userName
    }
    return render(request,'room.html', context)

def send(request):
    userName = request.POST['username']
    roomId = request.POST['room_id']
    message = request.POST['message']

    newMessage = Message.objects.create(value=message,user=userName, room=roomId)
    newMessage.save()

    return HttpResponse(f"the message is: "+message)