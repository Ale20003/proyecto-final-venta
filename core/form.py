from django import forms
from django.forms import ModelForm
from .models import Carro

class CarroForm(ModelForm):
    class Meta:
        model=Carro
        fields="__all__"
        widgets={
            'talla':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar una talla',
                    'class':'form-control'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese una descripcion del producto',
                    'class':'form-control'
                }
            ),
            'seccion':forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }