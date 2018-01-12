from django.conf.urls import url
from . import views
from .views import BooksListView


urlpatterns = [
    url(r'', BooksListView.as_view(), name='book_list'),
    
    url(r'^SignUp/$', views.SignUpView.as_view(), name='create-user'),
    url(r'^SignIn/$', views.SignInView.as_view(), name='log-user'),
    
]