from ..Models.models import SalePlace
from ..Schemas.serializers import SalePlaceSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

class SalePlaceMethods(viewsets.ModelViewSet):
    queryset = SalePlace.objects.all()
    serializer_class = SalePlaceSerializer