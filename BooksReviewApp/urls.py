from django.conf.urls import url
from . import views
from .views import BooksListView


urlpatterns = [
    url(r'', BooksListView.as_view(), name='book_list'),
    
]