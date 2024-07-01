from django.shortcuts import render,redirect
from .models import   Usuario,Manga,capitulo

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
    mangas = Manga.objects.all()
    return render(request, "crud.html", {"mangas": mangas})

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
