from django.contrib import admin

from src.apps.book.models import Book

class BookAdmin(admin.ModelAdmin[Book]): ...
