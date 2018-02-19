from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from books.views.books_view import BookViewSet
from books.factories import BookFactory
from books.models import Book
from users.factories import UserFactory

BASE_URL = '/api/v1/books/'


class TestBooksApiEndpoint(APITestCase):
    """
    Tests for books api endpoint.
    """

    def setUp(self):
        """
        Setup before each test cases.
        """
        self.factory = APIRequestFactory()
        self.view = BookViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update',
                                         'patch': 'partial_update', 'delete': 'destroy'})

    def test_update_is_not_allowed(self):
        """
            Make sure that put action is not allowed.
        """
        book = BookFactory()
        new_title = 'new title'
        url = '{0}{1}'.format(BASE_URL, book.id)
        request = self.factory.put(url, {'title': new_title}, format='json')

        response = self.view(request, pk=book.id)

        # Assert that method is not allowed, no data has been returned and the object was not changed.
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEquals(response.data, {'detail': 'Method "PUT" not allowed.'})

        book.refresh_from_db()

        self.assertNotEquals(book.title, new_title)

    def test_delete(self):
        """
            Make sure that delete method is working.
        """
        # Create a book via book factory.
        book = BookFactory()

        url = '{0}{1}'.format(BASE_URL, book.id)
        request = self.factory.delete(url)

        response = self.view(request, pk=book.id)

        # Assert that method is not allowed and no data has been returned. and the object was not changed.
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)

        self.assertEquals(Book.objects.all().count(), 0)

    def test_create_action(self):
        """
         Make sure that create is working as expected.
        """
        book = BookFactory.build()
        author = UserFactory()

        book_json = {'title': book.title, 'price': book.price, 'short_description': 'this is a short description',
                     'author': author.id, 'isbn': '1012167402'}

        request = self.factory.post(BASE_URL, data=book_json, format='json')

        response = self.view(request)
        # Assert that method that a new object has been created, status code is 201, object details are returned.
        self.assertEquals(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(response.data['title'], book_json['title'])

        self.assertEquals(Book.objects.all().count(), 1)

    def test_partial_update(self):
        """
        Make sure that partial update is working.
        """
        book = BookFactory()
        new_title = 'new title'
        url = '{0}{1}'.format(BASE_URL, book.id)
        request = self.factory.patch(url, data={'title': new_title}, format='json')

        response = self.view(request, pk=book.id)

        # Assert that method that a new object has been created, status code is 201, object details are returned.
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['title'], new_title)

    def test_list(self):
        """
        Make sure that list method is working as expected.
        """
        number_of_books = 5
        author = UserFactory()
        # Use the same author, rather than creating a new instance for each one.
        _ = BookFactory.create_batch(number_of_books, author=author)
        request = self.factory.get(BASE_URL, format='json')

        self.view = BookViewSet.as_view({'get': 'list'})

        response = self.view(request)

        self.assertEqual(len(response.data), number_of_books)

    def test_retrieve(self):
        """
        Make sure that retrieve is working as expected.
        """
        book = BookFactory.create()
        self.view = BookViewSet.as_view({'get': 'retrieve'})

        url = "{0}{1}".format(BASE_URL, book.id)

        request = self.factory.get(url)

        response = self.view(request, pk=book.id)

        self.assertEqual(response.data['id'], book.id)
