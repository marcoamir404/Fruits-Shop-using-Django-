from django.db import models
# models.Model class defines all the common characteristics and behavior from django

class Products(models.Model):
    objects = None
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

#aban0beatdjang0
