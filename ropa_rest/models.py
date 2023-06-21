from django.db import models

# Create your models here.
    
class Compra(models.Model):
    idcompra=models.AutoField(primary_key=True)
    producto=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    cantidad=models.IntegerField()

    def __str__(self):
        return self.producto
    
class Comuna(models.Model):
    idcomuna = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado =models.IntegerField()

    def __str__(self):
        return self.descripcion

class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre    