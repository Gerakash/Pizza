# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import date

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
    image = models.ImageField()
    title = models.CharField(max_length=40)
    description = models.TextField()

class Order(models.Model):
    statuses = (
        ('pending','pending'),
        ('in_process','in_process'),
        ('delivered','delivered'),
        ('not_delivered','not_delivered')
    )
    payment_methods = (
        ('Nal','Nal'),
        ('Wall','Wall')
    )

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    payment_type = models.CharField(max_length=20,choices=payment_methods)
    status = models.CharField(max_length=40,choices=statuses,default='in_process')
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()


class Documents(models.Model):
    file = models.FileField()


class Profile(models.Model):
    genders = (
        ('Male','Male'),
        ('Female','Female')
    )

    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField()
    full_name = models.CharField(max_length=60)
    birth_date = models.DateField(default=date.today())
    phone = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    wallet = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)













