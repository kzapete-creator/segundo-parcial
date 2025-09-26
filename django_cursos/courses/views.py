
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video, Estudiante
from .forms import VideoForm, EstudianteForm

def videos_view(request):
    videos = Video.objects.order_by('-publicado')
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:videos'))
    else:
        form = VideoForm()
    return render(request, 'courses/videos_list.html', {'videos': videos, 'form': form, 'page_title': 'Videos'})

def usuarios_view(request):
    usuarios = Estudiante.objects.order_by('-creado')
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:usuarios'))
    else:
        form = EstudianteForm()
    return render(request, 'courses/usuarios_list.html', {'usuarios': usuarios, 'form': form, 'page_title': 'Usuarios'})

def creditos_view(request):
    return render(request, 'courses/creditos.html', {
        'page_title': 'Créditos',
        'autor': 'Kimberly Marleni Zapet Enriquez',
        'universidad': 'Universidad Mariano Gálvez de Guatemala',
        'curso': 'Desarrollo Web (090-036)',
        'catedratico': 'Ing. Iván Antonio de León Fuentes',
        'semestre': 'Segundo 2025',
        'seccion/aula': '4',
    })
