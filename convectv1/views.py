import imp
from operator import mod
from tkinter.font import ROMAN
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


def demo(request):

    return render(request, 'aravind.html')

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'demo/home.html', context)

def room(request, pk):

    # room = None
    # for i in rooms:

    #     if i['id'] == int(pk):

    #         room = i

    room = Room.objects.get(id=pk)

    context = {'room':room}

    return render(request, 'demo/room.html',context)
