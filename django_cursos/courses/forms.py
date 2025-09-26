
from django import forms
from .models import Video, Estudiante

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url', 'categoria']
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 3})}

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre_completo', 'correo', 'telefono', 'interes']
