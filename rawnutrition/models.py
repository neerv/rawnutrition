from django.db import models


# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()