from os import name
from tkinter import CASCADE
from django.db import models

class Author (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        ordering = ['name', 'surname']

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

class BookReaders (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
            ordering = ['name', 'surname']

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

class Books (models.Model):
    name = models.CharField(max_length=100)
    year_of_published = models.DateField()
    author = models.ManyToManyField(Author)
    readers = models.ManyToManyField(BookReaders, null=True, blank=True)
    are_available = models.BooleanField(default=True)
    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'Name of the book: {self.name}; Date of published: {self.year_of_published}; Author of the book: {self.author}'