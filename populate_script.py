import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO_PROJECT.settings')

import django
django.setup()

import random
from users_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_second_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, second_name=fake_second_name, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating completed!")