from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^SendRequest/$', views.SendRequestView.as_view(), name='sendrequest'),
    url(r'^SignUp/$', views.SignUpView.as_view(), name='create-user'),
    url(r'^SignIn/$', views.SignInView.as_view(), name='log-user'),
    url(r'^LogOut/$', views.LogoutView.as_view(), name='logout'),
    url(r'^Search/$', views.SearchView.as_view(), name='search'),
    url(r'^Reviews/(?P<author_id>\d+)/$',views.BooksOfWriter.as_view(), name='reviews'),
    url(r'', views.HomeView.as_view(), name='home')
]