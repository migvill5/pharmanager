from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventoryHome, name="inventory_home"),
    ]