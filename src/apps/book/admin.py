from django.contrib import admin

from src.apps.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "published_date",
    ]


admin.site.site_title = "Abol"
admin.site.site_header = "Администрирование Abol"
admin.site.index_title = "Панель администрирования"
