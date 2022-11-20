import time
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Calculator
from .serializers import CalculationSerializer
from .calculation import Calculation


class CalculationTrigger(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Calculator.objects.all()
    serializer_class = CalculationSerializer


class CalculationList(APIView):
    http_method_names = ['get', 'post', 'head']

    def get(self, request):
        users = Calculator.objects.all()
        calc_serializer = CalculationSerializer(users, many=True)
        return Response(calc_serializer.data)

    def post(self, request):
        start_time = time.time()

        evolutionary_computing_calculation = Calculation(
            int(request.data['epoch_amount']),
            int(request.data['population_members_count']),
            int(request.data['begin_of_range']),
            int(request.data['end_of_range']),
            int(request.data['end_of_range']),
            int(request.data['elite_strategy_percentage']),
            3,
            2,
            'roulette_selection',
            'one_point'
        )

        calculation_result = evolutionary_computing_calculation.trigger()
        execution_time = time.time() - start_time

        return Response({
            'executionTime': execution_time,
            'x1': calculation_result[-1][1],
            'x2': calculation_result[-1][2],
            'fitFunVal': calculation_result[-1][3]
        }, status=status.HTTP_200_OK)
