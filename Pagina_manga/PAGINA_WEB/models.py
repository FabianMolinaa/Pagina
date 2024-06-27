from django.db import models

# Create your models here.
from django.db import models

  
class Usuario(models.Model):
    user = models.CharField(primary_key=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)+" "+str(self.email)    