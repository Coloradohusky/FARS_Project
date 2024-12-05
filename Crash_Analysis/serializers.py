from rest_framework_gis import serializers

from .models import Accident


class AccidentSerializer(
    serializers.GeoFeatureModelSerializer,
):
    class Meta:
        fields = ("id", "st_case")
        geo_field = "location"
        model = Accident