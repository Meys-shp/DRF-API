from django.shortcuts import render
from serializers import ProductSerializer, BrandSerializer, CategorySerializer
from rest_framework import viewsets
from models import Brand, Category, Product


class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
      pass

class ProductViewSet(viewsets.ModelViewSet):
    pass
