from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Product
from .serializers import ProductSerializer, MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

 

 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return Response(all_products)
