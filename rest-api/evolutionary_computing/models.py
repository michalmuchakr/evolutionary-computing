from django.db import models


# Create your models here.
class Calculator(models.Model):
    begin_of_range = models.CharField("begin_of_range", max_length=240)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.begin_of_range
