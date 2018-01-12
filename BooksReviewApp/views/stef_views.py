from django.shortcuts import render
from django.views.generic import ListView
from BooksReviewApp.models import Book


class SearchView(ListView):
    
    def get(self, request):
        books = []
        if request.GET.get('q'):
            book_name = request.GET.get('q')
            books = Book.objects.all().filter(name__icontains=book_name)
        return render(request, 'BooksReviewApp/Search.html', {"books":books})