from django.urls import path
from web import views 

urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    path("nomina", views.nomina, name="nomina"),
    path("alta", views.formulario, name="alta"),
    path("veterinaria", views.veterinaria, name="veterinaria"),
    path("alta_mascota", views.mascota, name="alta_mascota"),
    path("comentario", views.mensaje, name="comentario"),
    path("buscar_mascota", views.buscar_mascota, name="buscar_mascota"),
    path("buscar", views.buscar, )

    
]