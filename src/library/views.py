# coding=utf-8
import datetime

from django.db.models import Q
from django.views.generic import DetailView, ListView

from users.models import User
from .models import Book, Author, BookCopy


class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'book_list'
    paginate_by = 20


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'
    context_object_name = 'author_list'
    paginate_by = 20


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'


class BorrowedBookListView(ListView):
    template_name = 'book/borrowed_list.html'
    context_object_name = 'book_copy_list'

    def get_queryset(self):
        return (
            BookCopy.objects.filter(borrower=self.request.user.id)
            .filter(status__exact='l')
            .order_by('due_back')
        )


class AllUsersBorrowedBookListView(ListView):
    template_name = 'book/all_borrowed.html'
    context_object_name = 'book_copy_list'

    def get_queryset(self):
        return (
            BookCopy.objects.all().order_by('due_back'))


class SearchResultsView(ListView):
    context_object_name = 'book_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        book_queryset = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        )
        return book_queryset


class SearchEmailResultsView(ListView):
    model = BookCopy
    template_name = 'search_user.html'
    context_object_name = 'book_copy_list'

    def get_queryset(self):
        email = self.request.GET.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            return BookCopy.objects.filter(borrower=user)
        else:
            return BookCopy.objects.none()

