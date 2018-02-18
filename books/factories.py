from random import randrange
from decimal import Decimal

from faker import Faker

from factory import SubFactory, django
from factory import lazy_attribute_sequence

fake = Faker()


class BookFactory(django.DjangoModelFactory):
    """
        Factory for creating Book objects.
    """
    class Meta(object):
        """
        Meta class to specify which model to be considered when generating
        factories.
        """
        model = 'books.Book'

    author = SubFactory("users.factories.UserFactory")

    @lazy_attribute_sequence
    def title(self, number):
        """
        :param number: sequential number.
        :return: title with a sequential number.
        """
        return "title_{0}".format(number)

    @lazy_attribute_sequence
    def isbn(self, number):
        """
        :param number: sequential number.
        :return: unique isbn.
        """
        isbn = fake.isbn10(separator="")[:9]
        return "{0}{1}".format(isbn, number)

    price = Decimal(randrange(start=100))