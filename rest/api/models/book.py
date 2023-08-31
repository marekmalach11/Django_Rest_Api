from django.db import models
from . import Author


class Book(models.Model):
    title = models.CharField(max_length=64)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title