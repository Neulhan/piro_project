from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10)
    code = models.IntegerField()
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
    p_num = models.IntegerField(default=0)


class Guest(models.Model):
    name = models.CharField(max_length=10)
    b1 = models.BooleanField(default=False)
    b2 = models.BooleanField(default=False)
    b3 = models.BooleanField(default=False)
    b4 = models.BooleanField(default=False)
    b5 = models.BooleanField(default=False)
    b6 = models.BooleanField(default=False)
    b7 = models.BooleanField(default=False)
    b8 = models.BooleanField(default=False)
    b9 = models.BooleanField(default=False)
    b10 = models.BooleanField(default=False)
    score = models.IntegerField(default=0)