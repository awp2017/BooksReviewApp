from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^DeleteRequest/(?P<pk>[0-9]+)/$', views.DeleteRequest.as_view(), name='delete'),
    url(r'^AcceptRequest/(?P<pk>[0-9]+)/$', views.AcceptRequestView.as_view(), name='create-review1'),
    url(r'^CreateRequest/$', views.AcceptRequestView.as_view(), name='create-review'),
    url(r'^ApproveRequest/$', views.ApproveRequestView.as_view(), name='approverequest'),
    url(r'^SendRequest/$', views.SendRequestView.as_view(), name='sendrequest'),
    url(r'^SignUp/$', views.SignUpView.as_view(), name='create-user'),
    url(r'^SignIn/$', views.SignInView.as_view(), name='log-user'),
    url(r'^LogOut/$', views.LogoutView.as_view(), name='logout'),
    url(r'^Search/$', views.SearchView.as_view(), name='search'),
    url(r'^Reviews/(?P<author_id>\d+)/$',views.BooksOfWriter.as_view(), name='reviews'),
    url(r'^Details/(?P<review_id>\d+)/$',views.ReviewList.as_view(), name='details'),
    url(r'^TopBooks/$', views.TopBooks.as_view(), name='topbooks'),
    url(r'', views.HomeView.as_view(), name='home'),
]