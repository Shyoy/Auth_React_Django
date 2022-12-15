from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Product
from .serializers import ProductSerializer, MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status ,request
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

 

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET','POST','DELETE'])
# @permission_classes([IsAuthenticated])
def all_products(req):
    if req.method == 'GET':
        all_products = ProductSerializer(Product.objects.all(), many=True).data
        return Response(all_products)

    elif req.method == 'POST':
        serializer =  ProductSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)