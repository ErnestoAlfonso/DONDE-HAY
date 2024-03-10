from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=8)
    email = models.EmailField(max_length=254)
    #TODO : add password field


    def __str__(self):
        return self.username

    def clean(self):
        # Dont allow empty phone, email, or username entries.
        if self.username is None or self.phone is None or self.email is None:
            raise ValidationError(_("Por favor no deje ningún campo en blanco"))
        # Dont allow incorrect phone numbers.
        if self.phone[0] != '5': # Here we need to know how to prove that the phone number that the user is entering is a real phone number
            raise ValidationError(_("El número escrito no es correcto, por favor ingrese un número válido"))


class Location(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    direction = models.CharField(max_length=255)

class SalePlace(models.Model):
    name = models.CharField(max_length=255, default="")
    location = models.ForeignKey(Location, related_name = "location", on_delete=models.CASCADE)


class Product(models.Model):
    salePlace = models.ForeignKey(SalePlace, related_name="salePlace", default = None, primary_key = True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    price = models.FloatField(max_length = 45)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price is None or self.price < 0:
            raise ValidationError(_("El precio es un campo obligatorio y no puede ser negativo"))
    
    
        

