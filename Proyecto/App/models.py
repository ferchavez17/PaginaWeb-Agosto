from django.db import models

# Create your models here.
class Datos(models.Model):
    #no coloquen su dni
    #integerfield----->enteros
    DNI=models.IntegerField(primary_key=True)
    #Textfield----->cadenas de texto
    Apellido=models.TextField(max_length=30)
    Nombre=models.TextField(max_length=35)
    Edad=models.IntegerField()
    Fecha_Nacimiento=models.DateField()

    def __int__(self):
        self.DNI