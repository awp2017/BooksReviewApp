from django.shortcuts import render
from django.views.generic import ListView
from BooksReviewApp.models import Book
from BooksReviewApp.models import Writer
from BooksReviewApp.models import Book
from BooksReviewApp.models import Review
from .dan_views import WriterHelper

class SearchView(ListView):
    
    def get(self, request):
        books = []
        if request.GET.get('q'):
            book_name = request.GET.get('q')
            books = Book.objects.all().filter(name__icontains=book_name)
        return render(request, 'BooksReviewApp/Search.html', {"books":books})



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