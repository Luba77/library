from django.conf.urls import url
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

app_name = 'library'

urlpatterns = [
    url(r'books/$', BookListView.as_view(), name='book_list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'authors/$', AuthorListView.as_view(), name='author_list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),
]
