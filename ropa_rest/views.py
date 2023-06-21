from django.shortcuts import render
from .models import Compra,Cliente
from .serializers import CompraSerializer,ClienteSerializer
#clases propias de la API
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

##PARA LA AUTENTICACION
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

##PARA LAS FUNCIONES
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_compra(request):
    if request.method =='GET':
        query=Compra.objects.all()
        serializer = CompraSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST': 
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED) 
        else:
           return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))  
def detalle_compra(request, id):
    try:
        compra=Compra.objects.get(producto=id)
    except Compra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    if request.method =='GET':
        serializer = CompraSerializer(compra)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer = CompraSerializer(compra, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    if request.method =='DELETE':
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_cliente(request):
    if request.method =='GET':
        query=Cliente.objects.all()
        serializer = ClienteSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST': 
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED) 
        else:
           return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)     

def detalle_cliente(request, id):
    try:
        cliente=Cliente.objects.get(nombre=id)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    if request.method =='GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer = ClienteSerializer(cliente, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    if request.method =='DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login_admin(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("El Usuario No Existe") 
    pass_valid =check_password(password, user.password)
    if not pass_valid:
        return Response("Contraseña Incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)