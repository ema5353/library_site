from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
