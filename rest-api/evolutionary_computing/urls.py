from django.urls import path

from evolutionary_computing.views import CalculationList

urlpatterns = [
    path('compute/', CalculationList.as_view()),
]
