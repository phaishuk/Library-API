from typing import Type

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from book.models import Book
from book.serializers import BookSerializer, BookListSerializer


class BookPagination(PageNumberPagination):
    page_size = 5


class BookViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with book"""

    queryset = Book.objects.order_by("title")
    pagination_class = BookPagination

    def get_serializer_class(
        self,
    ) -> type[BookListSerializer | BookSerializer]:
        if self.action == "list":
            return BookListSerializer
        return BookSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        if self.action in ("create", "update", "partial_update", "destroy"):
            return [IsAdminUser()]
        return [IsAuthenticated()]
