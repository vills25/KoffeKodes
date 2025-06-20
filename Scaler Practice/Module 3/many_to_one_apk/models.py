# Django model for a many-to-one relationship between Author and Book
# In this example, each Author can have multiple Books, but each Book is associated with only one Author.

from django.db import models

class Author(models.Model): # author can have multiple book
    author_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE) # Books can have only one Author
    published_date = models.DateField()
    def __str__(self):
        return self.title

