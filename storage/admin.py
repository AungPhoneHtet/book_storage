from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.
admin.site.register(Publisher, Publisher.PublisherAdmin)
admin.site.register(Author, Author.AuthorAdmin)
admin.site.register(Book, Book.BookAdmin)