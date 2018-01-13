from django.shortcuts import render
from django.views.generic import ListView
from BooksReviewApp.models import Book
from BooksReviewApp.models import Writer
from BooksReviewApp.models import Book
from BooksReviewApp.models import Review
from BooksReviewApp.models import Comment
from .dan_views import WriterHelper

class SearchView(ListView, WriterHelper):
    
    def get(self, request):
        books = []
        books_review = []
        if request.GET.get('q'):
            book_name = request.GET.get('q')
            books = Book.objects.all().filter(name__icontains=book_name)
            for review in Review.objects.all():
                if review.book_pk in books:
                    books_review.append(review)
        return render(request, 'BooksReviewApp/Search.html', {"books_review":books_review})
    def get_context_data(self, **kwargs):
        context = super(SearchView,self).get_context_data()
        context['writer_list'] = self.getWriters()
        
        return context



class BooksOfWriter(ListView):
    model = Review
    context_object_name = 'book_list'
    template_name = 'BooksReviewApp/Reviews.html'
    def get_context_data(self, **kwargs):
        books = []
        reviews = []
        context = super(BooksOfWriter, self).get_context_data()
        context['writer_list'] = Writer.objects.order_by('-name')
        id_author = self.kwargs['author_id']
        author = Writer.objects.get(id=id_author)
        for book in Book.objects.all():
            if author in book.writers.all():
                books.append(book)
        for review in Review.objects.all():
            if review.book_pk in books:
                reviews.append(review)
        context['review_list'] = reviews
        return context  

class ReviewList(ListView):
    model = Review
    context_object_name = 'review_list'
    template_name = 'BooksReviewApp/ReviewDetails.html'
    def get_context_data(self, **kwargs):
        comments = []
        context = super(ReviewList, self).get_context_data()
        context['writer_list'] = Writer.objects.order_by('-name')
        id_review = self.kwargs['review_id']
        review = Review.objects.filter(id=id_review)
        context['review_list1'] = review
        context['comment_list'] = Comment.objects.filter(review_pk=review)
        return context
    