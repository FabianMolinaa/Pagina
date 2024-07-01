from django.contrib import admin
from .models import  Usuario, Manga, capitulo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Manga)
admin.site.register(capitulo)
