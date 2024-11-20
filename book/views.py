from django.shortcuts import render
from .models import Book, Author
from django.views.generic import ListView

class BookListView(ListView):
    queryset = Book.objects.defer("author__created_at").all().select_related("author")
    template_name = 'books.html'
