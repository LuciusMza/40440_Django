from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=256)   #equivalente de str
    comision = models.IntegerField()    #equivalente de int

class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()     #equivalente de email
    telefono = models.CharField(max_length=20)    #se puede hacer como IntegerField pero se suele usar CharField
    dni = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField()     #equivalente de fecha
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()     
    telefono = models.CharField(max_length=20)    #se puede hacer como IntegerField pero se suele usar CharField
    dni = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField()    
    bio = models.TextField()       #campo de texto sin límite (CharField ocupa menos espacio de memoria)

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateField()
    esta_aprobado = models.BooleanField(default=False)   #equivalente de verdadero o falso
    