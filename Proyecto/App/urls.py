from django.urls import path
# traemos el sector de las vistas "views"
'''
    ----->import inicio---> Sola esa funcion
    ----->import * --------> todas las funciones
'''
from .views import *

urlpatterns = [
    # generamos la ruta

    #-----> '' ---->primer pagina al ejecutar el server
    #--->Inicio ---> funcion de vistas
    #---> name="Inicio" --->Nombre para url de html
path('',Inicio,name='Inicio'),
path('nosotros/', nosotros, name='Nosotros'),
path('acerca/', Acerca, name='Acerca'),
path('registrar/', Registrar, name='Registrar')

 ]