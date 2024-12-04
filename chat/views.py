from django.shortcuts import render, redirect
from .models import Room

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def checkView(request):
    roomName = request.POST['room_name']
    userName = request.POST['user_name']
    if Room.objects.filter(name=roomName).exists():
        return redirect('/'+roomName+'/?user_name='+userName)
    else:
        newRoom = Room.objects.create(name=roomName)
        newRoom.save()
        return redirect('/'+roomName+'/?user_name='+userName)

def roomView(request,room):
    userName = ''
    if request.GET:
        userName = request.GET['user_name']
        print(userName)
    context = {
        'room': room,
        'user': userName
    }
    return render(request,'room.html', context)