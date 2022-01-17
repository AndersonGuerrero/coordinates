from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from core.models import Property, Location
from core.serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):

    serializer_class = PropertySerializer
    queryset = Property.objects
    permission_classes = (
        IsAuthenticated,
    )

    @action(
        methods=['get'],
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def visited(self, request, *args, **kwargs):
        houmer = request.GET.get('houmer')
        locations = Location.objects.filter(
            houmer_id=int(houmer)
        ).order_by('created_at')
        # podriamos filtrar por la ubicación del houmer..
        properties = Property.objects.all()
        properties_visited = []
        for p in properties:
            visit_time = 0
            times = 0
            for loc in locations:
                latitude = round(loc.latitude, 9)
                longitude = round(loc.longitude, 9)
                max_lat = 0
                min_lat = 0
                max_lon = 0
                min_lon = 0
                for x in p.full_limits:
                    lat, lon = x.split(',')
                    lat = round(float(lat), 9)
                    lon = round(float(lon), 9)
                    if abs(lat) > abs(max_lat):
                        max_lat = lat

                    if abs(lat) < abs(min_lat) or min_lat == 0:
                        min_lat = lat

                    if abs(lon) > abs(max_lon):
                        max_lon = lon

                    if abs(lon) < abs(min_lon) or min_lon == 0:
                        min_lon = lon
                if (
                    abs(latitude) <= abs(max_lat) and
                    abs(latitude) >= abs(min_lat) and
                    abs(longitude) <= abs(max_lon) and
                    abs(longitude) >= abs(min_lon)
                ):
                    visit_time = loc.created_at
                    propertie_visited = p
                elif visit_time:
                    t = loc.created_at - visit_time
                    times = round(t.seconds / 60)
                    visit_time = 0
            data = self.serializer_class(
                propertie_visited
            ).data
            data.update({'visiting_time': times if times else 'on property'})
            properties_visited.append(data)
        return Response(
            properties_visited,
            status=status.HTTP_200_OK
        )
