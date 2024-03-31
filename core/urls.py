from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from products.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductListView,
    ProductUpdateView,
    ProductDetailView,
    ProductReactivateView
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-token-auth/', obtain_auth_token),
                  path('products/', ProductListView.as_view(), name='product-list'),
                  path('products/create/', ProductCreateView.as_view(), name='product-create'),
                  path('products_detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
                  path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
                  path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
                  path('products/reactivate/<int:pk>/', ProductReactivateView.as_view(), name='product-reactivate'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
