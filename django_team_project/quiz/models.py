from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10)
    code = models.IntegerField()
    p1 = models.IntegerField(default=-1)
    p2 = models.IntegerField(default=-1)
    p3 = models.IntegerField(default=-1)
    p4 = models.IntegerField(default=-1)
    p5 = models.IntegerField(default=-1)
    p6 = models.IntegerField(default=-1)
    p7 = models.IntegerField(default=-1)
    p8 = models.IntegerField(default=-1)
    p9 = models.IntegerField(default=-1)
    p10 = models.IntegerField(default=-1)


class Guest(models.Model):
    name = models.CharField(max_length=10)
    p1 = models.IntegerField(default=-1)
    p2 = models.IntegerField(default=-1)
    p3 = models.IntegerField(default=-1)
    p4 = models.IntegerField(default=-1)
    p5 = models.IntegerField(default=-1)
    p6 = models.IntegerField(default=-1)
    p7 = models.IntegerField(default=-1)
    p8 = models.IntegerField(default=-1)
    p9 = models.IntegerField(default=-1)
    p10 = models.IntegerField(default=-1)


