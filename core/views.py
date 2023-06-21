from django.shortcuts import render, redirect
from .models import Carro 
from .form import CarroForm


def inicio(request):
    return render(request,"core/inicio.html")

def hombre(request):
    return render(request,"core/hombre.html")

def mujer(request):
    return render(request,"core/mujer.html")

def niño(request):
    return render (request,"core/niño.html")

def formulario(request):
    return render (request,"core/formulario.html")

def carrito(request):
    carrito = Carro.objects.all()
    return render(request,"core/carrito.html",{"carrito":carrito})

def catalogo(request):
    return render(request,"core/catalogo.html")

def inicioadmin (request):
    carrito=Carro.objects.all()
    return render(request,"core/admin/inicioadmin.html",{"carrito":carrito})

def guardar_ropa(request):
    form = CarroForm
    mensaje = ""
    if request.method=='POST':
        form =CarroForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion=request.POST.get('descripcion', None)
            if descripcion in Carro.objects.values_list('descripcion', flat=True):
                mensaje= "Esta prenda ya esta registrada"
            else:
                form.save()
                mensaje= "Datos guardados exitosamente"
                    
    return render(request, "core/admin/guardar_ropa.html",{"form":form,"mensaje":mensaje})
    
    
def modificar_ropa(request,id):
    carrito=Carro.objects.get(descripcion=id)
    mensaje= ""
    if request.method=='POST':
        form=CarroForm(request.POST, request.FILES, instance=carrito)
        if form.is_valid():
             form.save()
             mensaje="Datos Modificados Correctamente"
             return redirect(to="inicioadmin")
    else:
        return render(request,"core/admin/modificar_ropa.html", {"form":CarroForm(instance=carrito), "mensaje":mensaje})      

def delete_ropa(request, id):
    Carrito=Carro.objects.get(descripcion=id)
    Carrito.delete()
    return redirect(to="inicioadmin")
    
