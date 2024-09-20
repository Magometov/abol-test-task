from django.http import Http404
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from src.apps.api.serializers.books import BookSerializer
from src.apps.book.models import Book


@extend_schema(
    request=BookSerializer,
    responses={
        201: BookSerializer,
        422: BookSerializer.errors,
    },
)
@api_view(["POST"])
def create_book_view(request: Request) -> Response:
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@extend_schema(
    request=BookSerializer,
    responses={
        200: BookSerializer,
        404: None,
        422: BookSerializer.errors,
    },
)
@api_view(["PATCH"])
def update_specific_book_view(request: Request, book_id: int) -> Response:
    try:
        book = get_object_or_404(Book, id=book_id)
    except Http404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@extend_schema(
    request=BookSerializer,
    responses={
        200: None,
        404: None,
    },
)
@api_view(["DELETE"])
def delete_specific_book_view(request: Request, book_id: int) -> Response:
    try:
        book = get_object_or_404(Book, id=book_id)
    except Http404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_books_view(request: Request) -> Response:
    data = Book.objects.all()
    serializer = BookSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={
        200: None,
        404: None,
    },
)
@api_view(["GET"])
def get_specific_book_view(request: Request, book_id: int) -> Response:
    try:
        data = get_object_or_404(Book, id=book_id)
    except Http404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(data)
    return Response(serializer.data)
