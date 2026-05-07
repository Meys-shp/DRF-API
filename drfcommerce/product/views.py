from django.shortcuts import render
from pygments.lexers.sql import SqlLexer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product,ActiveQueryset
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqliteConsoleLexer
from sqlparse import format


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
    a Simple Viewlet for Product Model
    """
    # queryset = Product.objects.all()
    queryset = Product.objects.active()
    lookup_field = "slug"

    @extend_schema(responses={200: ProductSerializer()})
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['get'], detail=False, url_path=r'category/(?P<category>\w+)/all', url_name='all')
    def list_product_by_category(self, request, category=None):
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)

    # def retrieve(self, request, slug=None):
    #     queryset = self.queryset.filter(slug=slug)
    #
    #     serializer = ProductSerializer(queryset, many=True)
    #
    #     sqlformatted = format(
    #         str(queryset.query),
    #         reindent=True
    #     )
    #
    #     print(
    #         highlight(
    #             sqlformatted,
    #             SqliteConsoleLexer(),
    #             TerminalFormatter()
    #         )
    #     )
    #
    #     return Response(serializer.data)
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug).select_related("category"), many=True)
        data=Response(serializer.data)
        q=list(connection.queries)
        print(len(q))
        for qs in  q:
            sqlformatted = format(str(qs["sql"]),reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return data
