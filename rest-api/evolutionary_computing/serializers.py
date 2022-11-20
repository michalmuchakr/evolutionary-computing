from .models import Calculator
from rest_framework import serializers


class CalculationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calculator
        fields = ['begin_of_range']

