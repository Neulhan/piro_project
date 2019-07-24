from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=6)
    p1 = models.CharField(max_length=10)
    p2 = models.CharField(max_length=10)
    p3 = models.CharField(max_length=10)
    p4 = models.CharField(max_length=10)
    p5 = models.CharField(max_length=10)
    p6 = models.CharField(max_length=10)
    p7 = models.CharField(max_length=10)
    p8 = models.CharField(max_length=10)
    p9 = models.CharField(max_length=10)
    p10 = models.CharField(max_length=10)


class Guest(models.Model):
    name = models.CharField(max_length=10)
    p1 = models.CharField(max_length=10)
    p2 = models.CharField(max_length=10)
    p3 = models.CharField(max_length=10)
    p4 = models.CharField(max_length=10)
    p5 = models.CharField(max_length=10)
    p6 = models.CharField(max_length=10)
    p7 = models.CharField(max_length=10)
    p8 = models.CharField(max_length=10)
    p9 = models.CharField(max_length=10)
    p10 = models.CharField(max_length=10)

