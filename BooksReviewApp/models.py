# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone
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

class Review(models.Model):
    author_pk = models.ForeignKey('auth.User')
    book_pk = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.review_text

class Comment(models.Model):
    user_pk = models.ForeignKey('auth.User')
    review_pk = models.ForeignKey(Review, on_delete=models.CASCADE)
    comm_text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comm_text