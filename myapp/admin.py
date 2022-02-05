from logging import Filter
from django.contrib import admin
from .models import Books, Author, BookReaders


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(BookReaders)
class BookReadersAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_of_published', 'are_available']
    list_filter = ['name', 'year_of_published']



