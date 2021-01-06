from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py 
from administrativo.forms import *

# Create your views here.

def index(request):
    # return HttpResponse("Hola mundo desde Python")
    return HttpResponse("Hola mundo desde Python<br/>%s" % (request.path))

def listadoEstudiantes(request):
    """
    Listar los registros del modelo Estudiante, 
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'listadoEstudiantes.html', informacion_template)
    

def listadoEstudiantesDos(request):
    """
    Listar los registros del modelo Estudiante, 
    obtenidos de la base de datos.
    """
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'listadoEstudiantesDos.html', informacion_template)
 

def crearEstudiante(request):
    """
    """
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoEstudiantesDos)
    else:
        formulario = EstudianteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante.html', diccionario) 


def editarEstudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoEstudiantesDos)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEstudiante.html', diccionario) 

def crearTelefono(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoForm(estudiante, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            estudiante = Estudiante.objects.get(pk=request.POST['estudiante'])
            instance.estudiante = estudiante
            instance.save()
            return redirect(listadoEstudiantesDos)
    else:
        formulario = NumeroTelefonicoForm(estudiante)
    diccionario = {'formulario': formulario, 'estudiante': estudiante}

    return render(request, 'crearNumeroTelefonico.html', diccionario) 

