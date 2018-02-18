import faker

from factory import SubFactory, django
from factory import Sequence, lazy_attribute, lazy_attribute_sequence


class UserFactory(django.DjangoModelFactory):
    """
        Factory for creating users.
    """
    class Meta(object):
        """
        Meta class to specify which model to be considered when generating
        factories.
        """
        model = 'auth.User'

    first_name = lazy_attribute(lambda o: faker.Faker().first_name())
    last_name = lazy_attribute(lambda o: faker.Faker().last_name())

    @lazy_attribute_sequence
    def username(self, number):
        """
            Create username from first name and last name and add a number to it to make it unique.
        """
        return self.first_name + "." + self.last_name + str(number)

    email = Sequence(lambda n: 'user{0}@example.com'.format(n))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = 'test123'
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user
