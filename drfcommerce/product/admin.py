from django.contrib import admin

from drfcommerce.product.models import Product,Brand,Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
