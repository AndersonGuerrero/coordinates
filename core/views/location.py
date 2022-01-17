from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Location
from core.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects
    permission_classes = (
        IsAuthenticated,
    )
