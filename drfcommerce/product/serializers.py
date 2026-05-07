from rest_framework import serializers

from drfcommerce.product.models import Product, Category, Brand, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')

    class Meta:
        model = Category
        # exclude = ('id',)
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        # fields = '__all__'
        # exclude = ('id',)
        fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(read_only=True, source='brand.name')
    category = CategorySerializer(read_only=True)
    product_line = ProductLineSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "description", "slug", "brand_name", "category", "product_line")
