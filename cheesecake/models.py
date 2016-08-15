# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Cake(models.Model):
    CakeName = models.CharField(max_length=100)
    CakeContent = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__ (self):
        return  self.CakeName


class VisitorTime (models.Model):
    number = models.IntegerField()
    time= models.DateTimeField(auto_now_add=True) 

   fff
        
        