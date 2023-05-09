from django.db import models

# Create your models here.
class Coordinates(models.Model):
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
