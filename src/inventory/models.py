from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=600, null=True)
    barcode = models.CharField(max_length=30, null=False)
    data_created = models.DateField(auto_now=True)

class Laboratory(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=600, null=True)
    address1 = models.CharField(max_length=200, null=False)
    address2 = models.CharField(max_length=200, null=False)
    data_created = models.DateField(auto_now=True)

class Supplier(models.Model):
    ame = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=600, null=True)
    address = models.CharField(max_length=200, null=False)
    data_created = models.DateField(auto_now=True)


