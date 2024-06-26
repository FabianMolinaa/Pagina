from django.shortcuts import render
from .models import Genero, Usuario

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def biblioteca(request):
    return render(request, "biblioteca.html")

def Akuyaku(request):
    return render(request,"vista/Akuyaku_Reijou.html")

def black_clover(request):
    return render(request,"vista/black_clover.html")

def blue_lock(request):
    return render(request,"vista/blue_lock.html")

def chainsaw_man(request):
    return render(request,"vista/chainsaw_man.html")

def jujutsu_kaisen(request):
    return render(request,"vista/jujutsu_kaisen.html")

def sousou(request):
    return render(request,"vista/sousou_no_frieren.html")

def spy(request):
    return render(request,"vista/spyxfamily.html")

def yofukashi(request):
    return render(request,"vista/yofukashi.html")

def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "crud.html", context)