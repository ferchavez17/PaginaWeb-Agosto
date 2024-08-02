# importamos todos los forms
from django import forms
# importamos los modelos de models
from .models import Datos

# generamos un formulario para importar html
class NuevoDatos(forms.ModelForm):
    class Meta:
        # traemos la tabla
        model = Datos
        # traemos todos los atributos de la tabla
        fields= '__all__'