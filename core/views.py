# render: función que combina una plantilla con datos y arma la respuesta HTTP
from django.shortcuts import render
# connection: objeto de Django que expone la configuración de la base de datos activa
from django.db import connection
# Servicio: NUEVO — el modelo del paso 02, importado desde este mismo directorio (el punto = "esta app")
from .models import Servicio

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

# servicios: la vista que responde en /servicios/
def servicios(request):
    # .objects.all(): pide TODOS los servicios a MySQL (Django lo traduce a SELECT * FROM core_servicio)
    lista_servicios = Servicio.objects.all()
    # entrega la lista a la plantilla con el nombre "servicios", igual que en la Semana 3
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})