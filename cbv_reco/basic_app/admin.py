from django.contrib import admin
from basic_app.models import PetOwner, Product, Pet

# Register your models here.
admin.site.register([PetOwner, Product, Pet])
