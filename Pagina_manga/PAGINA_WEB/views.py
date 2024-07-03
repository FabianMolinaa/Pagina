from django.shortcuts import render,redirect
from .models import Usuario,Manga,capitulo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

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

@login_required
def crud(request):
    mangas = Manga.objects.all()
    return render(request, "crud.html", {"mangas": mangas})

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            loginn(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"index.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
            }
            return render(request,"login.html",context)
    else:
        context = {

        }
        return render(request,"login.html",context)

def salir(request):
    logout(request)
    return redirect("/")

def register(request):
    return render(request,'index.html')

def add_manga(request):
    if request.method != "POST":  
        mangas=Manga.objects.all()
        context={
           "mangas": mangas
        }
        return render(request,"crud.html",context)

    else:
        titulo=request.POST['txtTitulo']
        autor=request.POST['txtAutor']
        descripcion=request.POST['descripcion']

        manga=Manga.objects.create(
            titulo=titulo, 
            autor=autor,
            descripcion=descripcion)
        manga.save()

        mangas=Manga.objects.all()

        context={
           "mangas": mangas
        }
        return render(request,"crud.html",context)
    
def del_manga(request,titulo):
    try:
        manga = Manga.objects.get(titulo=titulo)
        manga.delete()

        mangas = Manga.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "mangas": mangas,
        }
        return render(request,"crud.html",context)
    except:
        mangas = Manga.objects.all()
        context = {
            "mensaje": "Error, Manga no encontrado...",
            "mangas": mangas,
        }
        return render(request, "crud.html", context)
