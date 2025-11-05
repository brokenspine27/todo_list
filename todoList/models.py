from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True) #Fecha del sistema al momento de crear el objeto
    descripcion = models.TextField()
    estado = models.CharField(max_length=30)