from django.db import models
from datetime import date


class Laboratory(models.Model):
    name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    data_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    movil = models.CharField(max_length=200, null=True)
    ruc = models.CharField(max_length=200, null=True)
    data_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class DosageForm(models.Model):
    MEASURES = (
        ('mL', 'mL'),
        ('cap', 'Capsula'),
        ('tab', 'Tableta'),
        ('grag', 'Gragea'),
        ('comp', 'Comprimido'),
        ('sob', 'Sobre'),
        ('amp-iny', 'Ampolla inyectable'),
        ('amp-beb', 'Ampolla bebible'),
        ('fras', 'Frasco'),
        ('bot', 'Botella'),
        ('ovuls', 'Ovulo'),
        ('sups', 'Supositorio'),
    )
    name = models.CharField(max_length=200, null=False)
    unit_number = models.IntegerField(default=0)
    unit_measure = models.CharField(max_length=200, null=False, choices=MEASURES)

    def __str__(self):
        return self.name + " x " + str(self.unit_number) + " ["+self.unit_measure+"]"


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=600, null=True)
    barcode = models.CharField(max_length=30, null=False)
    regsan = models.CharField(max_length=30, null=False, default="")
    quantity = models.IntegerField(default=0)
    data_created = models.DateField(auto_now=True)
    dosage_form = models.ForeignKey(DosageForm, null=True, on_delete=models.SET_NULL)
    laboratory = models.ForeignKey(Laboratory, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class ProductInput(models.Model):
    date_created = models.DateField(auto_now=True)
    batch = models.CharField(max_length=30, null=False, default="")
    date_production = models.DateField(default=date.today)
    date_expiry = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        string = self.product.name + " [ " + str(self.quantity) + " ]" + " <"+str(self.data_created)+">" + " => " + self.supplier.name 
        return string
