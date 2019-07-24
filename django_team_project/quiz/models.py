from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10)
    code = models.IntegerField(max_length=6)
    p1 = models.IntegerField(default=0)
    p2 = models.IntegerField(default=0)
    p3 = models.IntegerField(default=0)
    p4 = models.IntegerField(default=0)
    p5 = models.IntegerField(default=0)
    p6 = models.IntegerField(default=0)
    p7 = models.IntegerField(default=0)
    p8 = models.IntegerField(default=0)
    p9 = models.IntegerField(default=0)
    p10 = models.IntegerField(default=0)


class Guest(models.Model):
    name = models.CharField(max_length=10)
    b1 = models.BooleanField()
    b2 = models.BooleanField()
    b3 = models.BooleanField()
    b4 = models.BooleanField()
    b5 = models.BooleanField()
    b6 = models.BooleanField()
    b7 = models.BooleanField()
    b8 = models.BooleanField()
    b9 = models.BooleanField()
    b10 = models.BooleanField()
    score = models.IntegerField()

