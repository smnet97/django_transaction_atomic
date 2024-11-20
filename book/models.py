from django.db import models

class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        db_table = "authors"

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"