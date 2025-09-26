
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.videos_view, name='home'),
    path('videos/', views.videos_view, name='videos'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('creditos/', views.creditos_view, name='creditos'),
]
