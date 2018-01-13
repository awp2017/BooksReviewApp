from django.contrib import admin
from .models import Book, Writer, BookRequest, Review, Comment

admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(BookRequest)
admin.site.register(Review)
admin.site.register(Comment)