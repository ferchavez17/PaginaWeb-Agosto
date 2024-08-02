from django.shortcuts import render

# vistas de la url
        #def--->  PR para declarar una funcion
        #Inicio---> Nombre de la Funcion

from .formu import NuevoDatos
def Registrar(request):
    data={
        'forms':NuevoDatos()
    }
    # retornamos a la pagina web
    return render(request,"Pages/Registrar.html",data)

def nosotros(request):
    return render(request, 'Pages/Nosotros.html')

def Acerca(request):
    return render(request, 'Pages/Acerca.html')

def Inicio(request):
    return render(request, 'index.html')
