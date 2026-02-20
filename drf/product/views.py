from django.shortcuts import render
from rest_framework.response import Response

from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from rest_framework import viewsets
from .models import Brand, Category, Product
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    pass
