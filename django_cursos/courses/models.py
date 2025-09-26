
from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    url = models.URLField(help_text="URL de YouTube/Vimeo u hospedaje propio")
    categoria = models.CharField(max_length=80, blank=True)
    publicado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Estudiante(models.Model):  # Usuarios distintos al admin de Django
    nombre_completo = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    interes = models.CharField(max_length=80, blank=True, help_text="Área de interés, p. ej. Python, Web, Redes")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo}"
