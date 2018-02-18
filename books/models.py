from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models

from isbn_field import ISBNField


class Book(models.Model):
    """
        Class representing Book database table.
    """
    class Meta:
        db_table = 'books__book'
        ordering = ['id']

    # Attributes
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255)

    isbn = ISBNField(unique=True)

    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    short_description = models.TextField(blank=True, null=True)

    # Relations

    # As of Django 1.11, get_user_model can now be called at import time, even in modules that define models.
    author = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.CASCADE)

    # Properties
    @property
    def currency(self):
        return "{0}".format(settings.USED_CURRENCY)
