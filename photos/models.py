# coding: utf8
from django.db import models

# Create your models here.

class Typeface(models.Model):
    name = models.CharField(max_length=100)
    language = models.IntegerField() #语系：中文、英文
    type = models.IntegerField() #类型：楷书、行书
    style = models.IntegerField() #风格：毛笔、涂鸦
    brand = models.IntegerField() #厂家：汉仪、华文

class Photo(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    typeface = models.ForeignKey(Typeface)
    img_origin = models.ImageField(upload_to=str('origin'))





