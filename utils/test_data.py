from random import randint

from faker import Faker


class TestData:
    def __init__(self):
        self.faker = Faker(locale='en_US')

    @staticmethod
    def random_number(start: int = 1, end: int = 1000) -> int:
        return randint(start, end)

    def random_email(self) -> str:
        return self.faker.email()

    def random_first_name(self) -> str:
        return self.faker.first_name()

    def random_last_name(self) -> str:
        return self.faker.last_name()

    def random_phone_number(self) -> str:
        return self.faker.phone_number()

    def random_password(self) -> str:
        return self.faker.password()
