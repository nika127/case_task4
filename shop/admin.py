from django.contrib import admin
from .models import Author, Category, Book, Rental

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Rental)
