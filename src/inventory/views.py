from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inventoryHome(request):
    return HttpResponse('<h1>Inventory Home</h1>')
