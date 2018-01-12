# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
       
    class Meta:
        ordering = ('name',)
    
        
class Book(models.Model):
    name = models.CharField(max_length=30)
    writers = models.ManyToManyField(Writer)
    
    def __str__(self):
        return self.name
