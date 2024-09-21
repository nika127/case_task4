from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_on = models.DateField(auto_now_add=True)
    return_due = models.DateField()
    returned_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - Rented on {self.rented_on}"
