# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
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

class BookRequest(models.Model):
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    writer = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author.username + " asks for: " + self.writer + " " + self.book_name