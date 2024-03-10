from ..Models.models import Location
from ..Schemas.serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action


class LocationMethods(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer