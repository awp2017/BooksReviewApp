from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from BooksReviewApp.models import Book
from BooksReviewApp.models import Writer

class WriterHelper():

    def getWriters (self):
        return Writer.objects.order_by('-name')
        
class BooksListView(ListView, WriterHelper):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.order_by('-name')
    template_name = 'BooksReviewApp/Index.html'