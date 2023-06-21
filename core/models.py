from django.db import models

# Create your models here.
class Seccion(models.Model):
    idseccion =models.AutoField(primary_key=True)
    descripcion =models.CharField(max_length=50)
    estado= models.IntegerField()
    
    def __str__(self):
        return self.descripcion

class Carro(models.Model):
    idropa=models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    talla=models.CharField(max_length=2)
    seccion= models.ForeignKey(Seccion, on_delete=models.CASCADE)
    file=models.ImageField(upload_to="img/")
    def __str__(self):
        return self.descripcion
    
    
    
    
