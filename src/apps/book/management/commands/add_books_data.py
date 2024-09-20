# from datetime import datetime

# from django.core.management.base import BaseCommand

# from src.apps.book.management.commands.books_data import books_data
# from src.apps.book.models import Book


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         count = 0
#         for book in books_data:
#             title = book["title"].strip()
#             author = book["author"].strip()
#             # row_published_date = book["published_date"].split(".")
#             # published_date = datetime(
#             #     day=int(row_published_date[0]), month=int(row_published_date[1]), year=int(row_published_date[2])
#             # ).date()

#             if not Book.objects.filter(title=title).exists():
#                 Book.objects.create(
#                     title=title,
#                     author=author,
#                     published_date=published_date,
#                 )
#                 count += 1

#         return f"Созданно {count} из {len(books_data)} записей"
