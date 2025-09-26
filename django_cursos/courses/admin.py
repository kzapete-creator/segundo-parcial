from django.contrib import admin

admin.site.site_header  = "Cursos en línea — Panel"
admin.site.site_title   = "Cursos en línea"
admin.site.index_title  = "Administración"

# Afinar tus modelos existentes:
from .models import Video, Estudiante

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display   = ("titulo", "categoria", "publicado")
    search_fields  = ("titulo", "categoria")
    list_filter    = ("categoria", "publicado")   
    ordering       = ("-publicado",)
    readonly_fields = () 

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display   = ("nombre_completo", "correo", "interes", "creado")
    search_fields  = ("nombre_completo", "correo", "interes")
    list_filter    = ("interes", "creado")        
    ordering       = ("-created",) if hasattr(Estudiante, "created") else ("-creado",)
