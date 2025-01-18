import factory.fuzzy
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from app.users.models import UserProfile

faker = FakerFactory.create()


@register(_name='user_profile')
class UserProfileFactory(factory.Factory):
    class Meta:
        model = UserProfile

    id = factory.LazyFunction(lambda: faker.random_int())
    username = factory.LazyFunction(lambda: faker.word())
    email = factory.LazyFunction(lambda: faker.email())
    name = factory.LazyFunction(lambda: faker.name())
    yandex_access_token = factory.LazyFunction(lambda: faker.sha256())
    google_access_token = factory.LazyFunction(lambda: faker.sha256())
