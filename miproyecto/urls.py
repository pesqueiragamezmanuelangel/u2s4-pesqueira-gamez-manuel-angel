# admin: ya viene importado por defecto, no lo borres
from django.contrib import admin
# path, include: include permite delegar un grupo de rutas a otra app
from django.urls import path, include

urlpatterns = [
    # ruta del panel de administración, ya incluida por defecto
    path('admin/', admin.site.urls),
    # '': todo lo que llegue a la raíz del sitio se delega a core/urls.py
    path('', include('core.urls')),
]