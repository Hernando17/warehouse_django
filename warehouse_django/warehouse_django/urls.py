"""
URL configuration for warehouse_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='dashboard'),
    path('product', views.product_list, name='product.list'),
    path('product/create', views.product_create, name='product.create'),
    path('product/save', views.product_save, name='product.save'),
    path('product/edit/<int:id>', views.product_edit, name='product.edit'),
    path('product/update/<int:id>', views.product_update, name='product.update'),

    path('brand', views.brand_list, name='brand.list'),
    path('brand/create', views.brand_create, name='brand.create'),
    path('brand/save', views.brand_save, name='brand.save'),
    path('brand/edit/<int:id>', views.brand_edit, name='brand.edit'),
    path('brand/updat/<int:id>e', views.brand_update, name='brand.update'),
    path('brand/delete/<int:id>', views.brand_delete, name='brand.delete'),

    path('location', views.location_list, name='location.list'),
    path('location/create', views.location_create, name='location.create'),
    path('location/save', views.location_save, name='location.save'),
    path('location/edit/<int:id>', views.location_edit, name='location.edit'),
    path('location/update/<int:id>', views.location_update, name='location.update'),
    path('location/delete/<int:id>', views.location_delete, name='location.delete'),

    path('stock_move', views.stock_move_list, name='stock_move.list'),
    path('stock_move/create', views.stock_move_create, name='stock_move.create'),
    path('stock_move/save', views.stock_move_save, name='stock_move.save'),

    path('stock_quantity', views.stock_quantity_list, name='stock_quantity.list'),
    path('stock_quantity/create', views.stock_quantity_create, name='stock_quantity.create'),
    path('stock_quantity/save', views.stock_quantity_save, name='stock_quantity.save'),
    path('stock_quantity/edit/<int:id>', views.stock_quantity_edit, name='stock_quantity.edit'),
    path('stock_quantity/update/<int:id>', views.stock_quantity_update, name='stock_quantity.update'),
]
