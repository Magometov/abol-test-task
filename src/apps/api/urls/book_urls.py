from django.urls import path

from src.apps.api.views.book_views import (
    create_book_view,
    delete_specific_book_view,
    get_all_books_view,
    get_specific_book_view,
    update_specific_book_view,
)

urlpatterns = [
    path("create/", create_book_view),
    path("all/", get_all_books_view),
    path("get/<int:book_id>/", get_specific_book_view),
    path("update/<int:book_id>/", update_specific_book_view),
    path("delete/<int:book_id>/", delete_specific_book_view),
]
