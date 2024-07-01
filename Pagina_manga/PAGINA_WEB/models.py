from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
from django.db import models

  
class Usuario(models.Model):
    user = models.CharField(primary_key=True, validators=[MinLengthValidator(6)], max_length=12)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)+" "+str(self.email)    
    
class Manga(models.Model):
    titulo = models.CharField(primary_key=True, validators=[MinLengthValidator(5)], max_length=100)
    autor = models.CharField(max_length=30)
    descripcion = models.TextField(validators=[MinLengthValidator(30)], max_length=1000)
    
    def __str__(self):
        return str(self.titulo)
class capitulo(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='capitulos')
    numero_capitulo = models.IntegerField()
    titulo = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.manga)+" "+str(self.numero_capitulo)