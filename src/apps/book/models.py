from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=150)
    author = models.CharField(verbose_name="Автор", max_length=100)
    published_date = models.DateField(verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> str:
        return f"<Книга>: {self.title}"
