from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.
def inventoryHome(request):
    context = {}
    return render(request, 'inventory/main.html', context)

def storageHome(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/storage.html', context)

def productInput(request):
    pinputs = ProductInput.objects.all()
    context = {'pinputs': pinputs}
    return render(request, 'inventory/product_inputs.html', context)
