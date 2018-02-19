""" Create a couple of fake users. """
from django.core.management import BaseCommand

from users.factories import UserFactory

class Command(BaseCommand):
    """ Defines class to use with manage.py """
    def handle(self, *args, **options): #pylint: disable=too-many-locals
        """ Handler to create fake users """
        UserFactory.create_batch(10)
