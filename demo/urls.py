from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django_Rest_api.store.api_views import ProductList

import store.views as views
import store.api_views.ProductList

urlpatterns = [
    path('api/v1/products/', ProductList.as_view()),

    path('admin/', admin.site.urls),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('', views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
