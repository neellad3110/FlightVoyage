from rest_framework import serializers 
from .models import Country 


class FlightSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    number = serializers.CharField()
    name = serializers.CharField()
    seats = serializers.IntegerField()
    departure_date=serializers.DateField()
    departure_time=serializers.TimeField()
    journey_source=serializers.CharField()
    journey_destination=serializers.CharField()
    available_seats=serializers.IntegerField()

