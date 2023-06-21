from django.urls import path
from .views import lista_compra,lista_cliente,detalle_compra,detalle_cliente,login_admin

urlpatterns=[
    path('lista_compra', lista_compra, name="lista_compra"),
    path('lista_cliente', lista_cliente, name="lista_cliente"),
    path('detalle_compra/<id>', detalle_compra, name="detalle_compra"),
    path('detalle_cliente/<id>', detalle_cliente, name="detalle_cliente"),
    path('login_admin', login_admin, name="login_admin"),

]