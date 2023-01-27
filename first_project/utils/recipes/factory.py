from random import randint

from faker import Faker


def rand_ratio():
    return randint(500, 1280), randint(300, 900)


fake = Faker("pt_BR")


def make_recipe():
    width, height = rand_ratio()

    return {
        # "id": randint(1, 100),
        # "title": fake.sentence(nb_words=6),
        "description": fake.sentence(nb_words=12),
        "preparation_time": fake.random_number(digits=2, fix_len=True),
        "preparation_time_unit": 'Minutos',
        "servings": fake.random_number(digits=2, fix_len=True),
        "servings_unit": 'Porções',
        # "preparation_steps": fake.text(3000),
        "created_at": fake.date_time_this_year(),
        "author": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        },
        "category": {
            "name": fake.word(),
        },
        "cover": {
            "url": 'https://loremflickr.com/%s/%s/food' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    # from pprint import pprint
    # pprint(make_recipe())
    print(fake.sentence(nb_words=12))
