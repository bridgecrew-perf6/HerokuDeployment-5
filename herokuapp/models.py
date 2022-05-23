from django.db import models


class Bottles(models.Model):
    name = models.CharField(max_length=50)
    volume = models.DecimalField(decimal_places=2, max_digits=4)
    production_date = models.DateField()
