# render: función que combina una plantilla con datos y arma la respuesta HTTP
from django.shortcuts import render
# connection: objeto de Django que expone la configuración de la base de datos activa
from django.db import connection

# def: toda vista es una función que recibe "request" (la petición del navegador)
def inicio(request):
    # settings_dict: diccionario interno con ENGINE, HOST, NAME, etc. de la conexión activa
    info_bd = connection.settings_dict
    # contexto: los datos que la plantilla va a poder usar con {{ variable }}
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }
    # render: junta el template "core/inicio.html" con el contexto y devuelve el HTML final
    return render(request, 'core/inicio.html', contexto)

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