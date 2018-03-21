from django.db import models
from django.contrib import admin

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class PublisherAdmin(admin.ModelAdmin):
        list_display = ('name', 'address', 'email', 'website')

    class Meta:
        ordering=['name']

class Author(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class AuthorAdmin(admin.ModelAdmin):
        list_display = ('name', 'address', 'email', 'website')

    class Meta:
        ordering=['name']


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=16, default=0.00)

    def __str__(self):
        return self.title

    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'publisher', 'publication_date', 'price')
        list_filter = ('publication_date',)
        filter_horizontal = ('authors',)
        raw_id_fields = ('publisher',)

    class Meta:
        ordering=['title']


