import uuid

from django.conf import settings
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'author'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre"
    )

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    description = models.TextField(max_length=1000)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    class Meta:
        ordering = ['title', 'author']
        db_table = 'book'

    def __str__(self):
        return self.title


class BookCopy(models.Model):
    BOOK_STATUS = (
        ('un', 'Under maintenance'),
        ('ch', 'Checked out'),
        ('av', 'Available'),
        ('re', 'Reserved'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.PROTECT, null=True)
    publisher_info = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        blank=True,
        default='d')

    class Meta:
        ordering = ['due_back']
        db_table = 'bookcopy'

    def __str__(self):
        return '{} {}'.format(self.id, self.book.title)
