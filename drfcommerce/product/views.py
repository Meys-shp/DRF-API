from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    a Simple Viewlet for Category Model
    """
    queryset = Category.objects.all()

    @extend_schema(responses={200: CategorySerializer()})
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    a Simple Viewlet for Category Model
    """
    queryset = Brand.objects.all()

    @extend_schema(responses={200: BrandSerializer()})
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    a Simple Viewlet for Category Model
    """
    queryset = Product.objects.all()

    @extend_schema(responses={200: ProductSerializer()})
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
