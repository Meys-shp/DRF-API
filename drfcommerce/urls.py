from django.contrib import admin
from django.contrib.messages import api
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from drfcommerce.product import views
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView


router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'Brand', views.BrandViewSet)
router.register(r'Product', views.ProductViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(),name='swagger')
]
