from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from BooksReviewApp.models import Review
from BooksReviewApp.models import Book
from BooksReviewApp.models import Writer

class WriterHelper():

    def getWriters (self):
        return Writer.objects.order_by('-name')
        
class HomeView(ListView, WriterHelper):
    model = Review
    context_object_name = 'review_list'
    queryset = Review.objects.order_by('-date')[:3]
    template_name = 'BooksReviewApp/Index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data()
        context['writer_list'] = self.getWriters()
        
        return context
