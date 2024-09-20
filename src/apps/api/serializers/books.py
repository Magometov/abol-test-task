from datetime import date

from django.utils import timezone
from rest_framework import serializers

from src.apps.book.models import Book


class BookSerializer(serializers.ModelSerializer[Book]):
    published_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "published_date",
        ]

    def validate(self, data: dict[str, str | date]) -> dict[str, str | date]:
        published_date = data.get("published_date")
        if published_date and isinstance(published_date, date) and published_date.year > timezone.now().year:
            raise serializers.ValidationError("Не правильно указан год!")
        return data
