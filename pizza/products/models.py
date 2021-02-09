# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    categories = (
        ('vegan','vegan'),
        ('not_vegan','not_vegan'),
    )
    sizes = (
        ('small','small'),
        ('middle','middle'),
        ('great','great')
    )
    image = models.ImageField(blank=True,null=True,default='pizza_default.jpg')
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40,choices=categories)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    size = models.CharField(choices=sizes,max_length=20)


class AboutUs(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

class Order(models.Model):
    statuses = (
        ('pending','pending'),
        ('in_process','in_process'),
        ('delivered','delivered'),
        ('not_delivered','not_delivered')
    )
    status = models.CharField(max_length=40,choices=statuses,default='in_process')
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name




