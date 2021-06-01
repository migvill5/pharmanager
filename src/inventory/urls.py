from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventoryHome, name="inventory_home"),
    path('storage/', views.storageHome, name='storage'),
    path('productinput/', views.productInput, name='product_input'),
    ]