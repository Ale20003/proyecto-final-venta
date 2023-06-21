from django.urls import path
from .views import inicio, hombre, mujer, niño, formulario, carrito,catalogo, guardar_ropa, modificar_ropa, delete_ropa, inicioadmin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',inicio,name="inicio"),
    path('hombre/',hombre,name="hombre"),
    path('mujer/',mujer,name="mujer"),
    path('niño/',niño,name="niño"),
    path('formulario/',formulario,name="formulario"),
    path('carrito/',carrito,name="carrito"),
    path('catalogo/',catalogo, name="catalogo"),
    path('login/',LoginView.as_view(template_name="core/admin/login.html"), name="login"),
    path('logout/',LogoutView.as_view(template_name="core/inicio.html"), name="logout"), 
    path('guardar_ropa/',guardar_ropa,name="guardar_ropa"), 
    path('modificar_ropa/<id>',modificar_ropa,name="modificar_ropa"),    
    path('delete_ropa/<id>',delete_ropa,name="delete_ropa"), 
    path('inicioadmin/',inicioadmin,name="inicioadmin"),    
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
