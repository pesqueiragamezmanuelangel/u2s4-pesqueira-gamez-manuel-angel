# redirect: función para redirigir el navegador a otra URL después de guardar
from django.shortcuts import render, redirect, get_object_or_404
# login_required: decorador que exige sesión iniciada antes de entrar a la vista
from django.contrib.auth.decorators import login_required
# ServicioForm: el ModelForm que definiste en el paso 01
from .forms import ServicioForm
from .models import Servicio

# nueva función de vista, además de "inicio" que ya tenías
def servicios(request):
    # lista_servicios: datos de ejemplo en Python — todavía no vienen de MySQL
    lista_servicios = [
        {'nombre': 'Tutorías de programación', 'precio': 150},
        {'nombre': 'Diseño de logotipos', 'precio': 300},
        {'nombre': 'Repostería por encargo', 'precio': 120},
    ]
    # se la pasamos a la plantilla con la clave 'servicios'
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})

# @login_required: si nadie inició sesión, Django redirige solo al login
# (por ahora inicia sesión en /admin/ con tu superusuario; la Semana 6 trae tu propio login)
@login_required
def crear_servicio(request):
    # request.method: distingue si el navegador está pidiendo el formulario (GET) o enviándolo (POST)
    if request.method == 'POST':
        # ServicioForm(request.POST): reconstruye el formulario con los datos que el usuario tecleó
        form = ServicioForm(request.POST)
        # is_valid(): corre todas las validaciones del modelo (tipos, max_length, campos obligatorios)
        if form.is_valid():
            # commit=False: crea el objeto Servicio en memoria SIN guardarlo todavía en MySQL
            nuevo = form.save(commit=False)
            # propietario: se asigna aquí, no en el formulario, para que nadie pueda falsificarlo
            nuevo.propietario = request.user
            # save(): ahora sí guarda el registro completo en MySQL
            nuevo.save()
            # redirect('servicios'): evita reenvíos duplicados si el usuario recarga la página
            return redirect('servicios')
    else:
        # ServicioForm() sin datos: formulario vacío, para cuando la vista se abre por primera vez (GET)
        form = ServicioForm()
    # render: dibuja la plantilla, pasándole el formulario (vacío o con errores)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Nuevo servicio'})

@login_required
# pk: la clave primaria que Django extrae del pedazo <int:pk> de la URL (paso 05)
def editar_servicio(request, pk):
    # busca el Servicio con ese id; get_object_or_404 evita un try/except manual
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        # instance=servicio: le dice al formulario "actualiza ESTE registro, no crees uno nuevo"
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            # save(): al tener instance=, guarda los cambios sobre el mismo registro (UPDATE, no INSERT)
            form.save()
            return redirect('servicios')
    else:
        # instance=servicio sin datos de POST: precarga el formulario con los valores actuales
        form = ServicioForm(instance=servicio)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Editar servicio'})

@login_required
def eliminar_servicio(request, pk):
    # busca el registro exacto a borrar, igual que en editar_servicio
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        # delete(): borra la fila de MySQL de verdad; solo se ejecuta si el método fue POST
        servicio.delete()
        return redirect('servicios')
    # si es GET, solo muestra la pantalla de "¿Seguro?" — todavía no borra nada
    return render(request, 'core/servicio_confirm_delete.html', {'servicio': servicio})