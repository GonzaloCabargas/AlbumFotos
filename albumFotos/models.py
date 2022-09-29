from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo', null= True)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='fotos/', verbose_name="imagen", null=True)
    def __str__(self):
        return self.titulo