from django.db import models

# Create your models here.


class PetOwner(models.Model):
    name = models.CharField(max_length=256)
    pet = models.CharField(max_length=256)  # this shoudl be updted

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    weight = models.PositiveIntegerField()
    buyer = models.ForeignKey(
        PetOwner, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(
        PetOwner, related_name='pets', on_delete=models.CASCADE)

    def __str__(self):
            return self.name
