from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'shop/book_list.html'  # путь к шаблону

class BookDetailView(DetailView):
    model = Book
    template_name = 'shop/book_detail.html'  # путь к шаблону
