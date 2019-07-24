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
    b1 = models.IntegerField(default=0)
    b2 = models.IntegerField(default=0)
    b3 = models.IntegerField(default=0)
    b4 = models.IntegerField(default=0)
    b5 = models.IntegerField(default=0)
    b6 = models.IntegerField(default=0)
    b7 = models.IntegerField(default=0)
    b8 = models.IntegerField(default=0)
    b9 = models.IntegerField(default=0)
    b10 = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

