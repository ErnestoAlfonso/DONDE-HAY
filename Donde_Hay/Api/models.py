from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.

# class UserManager(models.Manager):
#     def create_user(self, username, email, phone, password):
#         user = self.create(username=username, email=email, phone=phone, password=password)
#         return user


class User(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=8)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.username

    def clean(self):
        # Dont allow empty phone, email, or username entries.
        if self.username is None or self.phone is None or self.email is None:
            raise ValidationError(_("Por favor no deje ningún campo en blanco"))
        # Dont allow incorrect phone numbers.
        if self.phone[0] != '5': # Here we need to know how to prove that the phone number that the user is entering is a real phone number
            raise ValidationError(_("El número escrito no es correcto, por favor ingrese un número válido"))



class Publication(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    date_time = models.DateTimeField()
    comments = models.JSONField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title



class Product(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    name_of_product = models.CharField(max_length = 255)
    price = models.FloatField(max_length = 45)

    def __str__(self):
        return self.name_of_product

    def clean(self):
        if self.price is None or self.price < 0:
            raise ValidationError(_("El precio es un campo obligatorio y no puede ser negativo"))
    
    
        

