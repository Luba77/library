from django.views.generic import DetailView, ListView

from .models import Book, Author


class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'book_list'
    paginate_by = 20


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'
    context_object_name = 'author_list'
    paginate_by = 20


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'
    context_object_name = 'author'
