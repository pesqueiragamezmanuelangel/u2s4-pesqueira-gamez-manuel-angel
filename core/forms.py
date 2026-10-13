# forms: trae las herramientas de Django para construir formularios
from django import forms
# Servicio: el modelo de la Unidad 2, importado desde este mismo directorio
from .models import Servicio

# ValidationError: la excepción que Django usa para reportar un error de validación
from django.core.exceptions import ValidationError

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['titulo', 'descripcion', 'precio', 'categoria']

    # clean_precio: Django lo llama automáticamente al validar el campo "precio"
    def clean_precio(self):
        # self.cleaned_data: diccionario con los valores ya convertidos a su tipo de Python
        precio = self.cleaned_data['precio']
        # regla propia: rechazar precios en cero o negativos, algo que DecimalField no revisa solo
        if precio <= 0:
            # ValidationError: si se dispara, el formulario se considera inválido y muestra este mensaje
            raise ValidationError('El precio debe ser mayor a 0.')
        # si no se disparó el error, hay que devolver el valor limpio para que el formulario lo use
        return precio