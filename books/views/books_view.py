from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from books.models import Book
from books.serializers.books_serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, editing and deleting book instances.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related('author')
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'isbn')
