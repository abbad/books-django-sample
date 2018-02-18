from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
        Serializer for book model.
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'price', 'currency', 'short_description', )
