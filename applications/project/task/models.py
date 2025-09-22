from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=400, blank=False, null=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=500)