from django.db import models


# Create your models here.
class CalculatorResults(models.Model):
    created = models.DateField(auto_now_add=True)
    saved_result_record_id = models.CharField("x1", max_length=240)
    x1 = models.CharField("x1", max_length=240)
    x2 = models.CharField("x2", max_length=240)
    fit_fun = models.CharField("fit_fun", max_length=240)
    variation = models.CharField("fit_fun", max_length=240)

    def __str__(self):
        return self.fit_fun


class Calculator(models.Model):
    created = models.DateField(auto_now_add=True)
    execution_time = models.CharField("execution_time", max_length=240)
    x1 = models.CharField("x1", max_length=240)
    x2 = models.CharField("x2", max_length=240)
    fit_fun = models.CharField("fit_fun", max_length=240)
    problem_to_solve = models.CharField("fit_fun", max_length=240)
    variation = models.CharField("fit_fun", max_length=240)

    def __str__(self):
        return self.fit_fun
