from django.contrib import admin
from .models import Book, Writer, BookRequest

admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(BookRequest)
