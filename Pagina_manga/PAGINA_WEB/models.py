from django.db import models

# Create your models here.
from django.db import models

class MiModelo(models.Model):
    campo = models.CharField(max_length=100)