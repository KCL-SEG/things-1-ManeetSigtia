from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
