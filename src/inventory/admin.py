from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Laboratory)
admin.site.register(Supplier)
admin.site.register(ProductInput)
admin.site.register(DosageForm)