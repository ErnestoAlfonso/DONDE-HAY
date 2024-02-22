from django.contrib import admin
from .models import User, Product, Publication
# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_filter = ('username', 'phone', 'email')
    list_display = ('username', 'phone', 'email')

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('publication', 'name_of_product', 'price')
    list_display = ('publication', 'name_of_product', 'price')

@admin.register(Publication)
class PublicationModel(admin.ModelAdmin):
    list_filter = ('title', 'user', 'productos', 'latitud', 'longitud', 'date_time', 'comments')
    list_display = ('title', 'user', 'productos', 'latitud', 'longitud', 'date_time', 'comments')