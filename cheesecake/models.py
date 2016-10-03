# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Cake(models.Model):

    CakeName = models.CharField(max_length=100)
    Price = models.CharField(max_length=10,default="")
    CakeContent = models.TextField(blank=True)
    photo = models.URLField(blank=True,null=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__ (self):
        return  self.CakeName


class VisitorTime (models.Model):

    number = models.IntegerField(null=True)
    time= models.DateTimeField(auto_now_add=True,null=True) 


class Totalviewer (models.Model):

    totalviewer = models.IntegerField(null=True)
    time= models.DateTimeField(auto_now_add=True,null=True) 

class Comment(models.Model):

    Nickname = models.CharField(max_length=20,default="")
    Email = models.EmailField(max_length=100,default="")
    Flavor = models.ManyToManyField(Cake)
    Content = models.CharField(max_length = 500,default="")   
    Timepost =  models.DateTimeField(auto_now_add=True) 


    def __unicode__ (self):
        return  self.Nickname

    
class Buy(models.Model):

    Customer_name = models.CharField(max_length=20,default="")
    Address =  models.CharField(max_length=200,default="")
    Phonenumber = models.CharField(max_length=20,default="")
    Catchmethod = models.CharField(max_length=50,default="")
    Catchlocation = models.CharField(max_length=50,default="")
    Email = models.EmailField(max_length=100,default="")
    Buynumber = models.TextField(max_length=200,null=True)
    Timepost =  models.DateTimeField(auto_now_add=True,null=True)
    Cakeflavor = models.ManyToManyField(Cake)
    Totalprice = models.CharField(max_length=20,default="")

    def __unicode__ (self):
        return  self.Customer_name