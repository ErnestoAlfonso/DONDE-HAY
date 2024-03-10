from ..Models.models import Product
from ..Schemas.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

class ProductMethods(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer