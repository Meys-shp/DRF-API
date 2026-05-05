from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

class CategoryViewSet(viewsets.ViewSet):
    """
    a Simple Viewlet for Category Model
    """
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
