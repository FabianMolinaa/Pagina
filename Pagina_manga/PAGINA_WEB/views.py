from django.shortcuts import render,redirect
from .models import Usuario,Manga,capitulo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import UsuarioForm,CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required

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

def registro(request):
    data ={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],email=formulario.cleaned_data["email"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="index")
        data["form"]=formulario
    return render(request,"registration/registro.html",data)

def conectar(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"registration/login.html",context)
    else:
        context = {

        }
        return render(request,"registration/login.html",context)

def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')



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
