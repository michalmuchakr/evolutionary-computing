import time
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from matplotlib import pyplot as plt
import statistics

from .calculation.utils.generate_charts import make_chart, save_charts
from .models import CalculatorResults
from .serializers import CalculationResultsSerializer, CalculationSerieSerializer
from .calculation import Calculation


class CalculationTrigger(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = CalculatorResults.objects.all()
    serializer_class = CalculationResultsSerializer


class CalculationList(APIView):
    http_method_names = ['get', 'post', 'head']

    @staticmethod
    def get(request):
        users = CalculatorResults.objects.all()
        calc_serializer = CalculationResultsSerializer(users, many=True)
        return Response(calc_serializer.data)

    def post(self, request):
        # start timer
        start_time = time.time()

        calculation_result = self._calculate_evolutionary_computing(request)

        # calc execution_time
        execution_time = time.time() - start_time

        best_fit_fun_value_in_each_epochs = make_chart(calculation_result)
        save_charts(best_fit_fun_value_in_each_epochs)

        saved_result_record_id = self._save_calculation_best_result(
            execution_time,
            calculation_result,
            request.data['problem_to_solve']
        )

        self._save_calculation_epochs(saved_result_record_id, calculation_result)

        return Response({
            'executionTime': execution_time,
            'x1': calculation_result[-1][1],
            'x2': calculation_result[-1][2],
            'fitFunVal': calculation_result[-1][3]
        }, status=status.HTTP_200_OK)

    @staticmethod
    def _calculate_evolutionary_computing(request):
        evolutionary_computing_calculation = Calculation(
            int(request.data['epoch_amount']),
            int(request.data['best_members_selection_percentage']),
            int(request.data['population_members_count']),
            int(request.data['search_result_range_from']),
            int(request.data['search_result_range_to']),
            int(request.data['elite_percentage']),
            int(request.data['tournament_selection_groups_size']),
            int(request.data['cross_probability']),
            int(request.data['mutation_probability']),
            int(request.data['inversion_probability']),
            request.data['selection_method'],
            request.data['problem_to_solve'],
            request.data['crossing_kind'],
            request.data['mutation_method'],
            'goldstein_price'
        )

        return evolutionary_computing_calculation.trigger()

    @staticmethod
    def _save_calculation_best_result(execution_time, calculation_result, problem_to_solve):
        result_record = {
            'execution_time': execution_time,
            'x1': calculation_result[-1][1],
            'x2': calculation_result[-1][2],
            'fit_fun': calculation_result[-1][3],
            'problem_to_solve': problem_to_solve,
            'variation': calculation_result[-1][4],
        }

        serialized_result_record = CalculationSerieSerializer(data=result_record)

        if serialized_result_record.is_valid():
            saved_result_record = serialized_result_record.save()
            saved_result_record_id = saved_result_record.id
        else:
            return Response({
                'reason': 'sth went wrong!'
            }, status=status.HTTP_400_BAD_REQUEST)

        return saved_result_record_id

    @staticmethod
    def _save_calculation_epochs(saved_result_record_id, calculation_result):
        serialized_data = [CalculationResultsSerializer(data={
            'saved_result_record_id': saved_result_record_id,
            'x1': result_item[1],
            'x2': result_item[2],
            'fit_fun': result_item[3],
            'variation': calculation_result[-1][4],
        }) for result_item in calculation_result]

        for serialized_data_item in serialized_data:
            if serialized_data_item.is_valid():
                serialized_data_item.save()
            else:
                return Response({
                    'reason': 'sth went wrong!'
                }, status=status.HTTP_400_BAD_REQUEST)
