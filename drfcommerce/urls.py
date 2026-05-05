from django.contrib import admin
from django.contrib.messages import api
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from drfcommerce.product import views



router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
