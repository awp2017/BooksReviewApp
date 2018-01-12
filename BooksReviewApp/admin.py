from django.contrib import admin
from .models import Book
from .models import Writer

admin.site.register(Book)
admin.site.register(Writer)