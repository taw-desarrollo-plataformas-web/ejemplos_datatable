"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.listadoEstudiantesDos, 
            name='listadoEstudiantesDos'),
        path('inicio', views.index, name='index'),
        path('listado-estudiantes', views.listadoEstudiantes, 
            name='listadoEstudiantes'),
        path('listado-estudiantes-dos', views.listadoEstudiantesDos, 
            name='listadoEstudiantesDos'),
        path('crear-estudiante', views.crearEstudiante, 
            name='crearEstudiante'),
        path('editar-estudiante/<int:id>', views.editarEstudiante, 
            name='editarEstudiante'),
        path('crear-telefono/<int:id>', views.crearTelefono, 
            name='crearTelefono'),
]
