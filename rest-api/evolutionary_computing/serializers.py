from .models import CalculatorResults, Calculator
from rest_framework import serializers


class CalculationResultsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CalculatorResults
        fields = ['saved_result_record_id', 'x1', 'x2', 'fit_fun']


class CalculationSerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calculator
        fields = ['id', 'execution_time', 'x1', 'x2', 'fit_fun']
