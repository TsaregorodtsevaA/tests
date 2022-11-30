import unittest, pytest
from parameterized import parameterized, parameterized_class
from tests.first_functions import find_russian_visits
FIXTURE = [
    ([{'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}], [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]),

    ([{'visit':['Россия', 'Россия']}],
     [{'visit':['Россия', 'Россия']}]),

    ([{'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']}], []),

    ([], []),

    ([{'visit4': ['Россия', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']}],
     [])
]
class TestFunc1(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_find_russian_visits(self, a, etalon):
        result = find_russian_visits(a)
        self.assertEqual(result, etalon)

from tests.first_functions import find_unique_values
FIXTURE = [

]
def test_find_unique_values():
    result = find_unique_values(
    {'user1': [213, 213, 213, 15, 213],
   'user2': [54, 54, 119, 119, 119],
   'user3': [213, 98, 98, 35]})
    etalon ={213, 15, 54, 119, 98, 35}
    assert result == etalon

def test_find_unique_values2():
    result2 = find_unique_values(
    {'user2': [54, 54, 119, 119, 119],
     'user3': [213, 98, 98, 35]})
    etalon2 = {213, 54, 119, 98, 35}
    assert result2==etalon2

def test_find_unique_values1():
    result1 = find_unique_values(
    {'user1': [0, 0, 00, 0],
     'user2': [54, 54, 119, 119, 119],
     'user3': [213, 98, 98, 35]})
    etalon1 = {0, 00, 213, 54, 119, 98, 35}
    assert result1==etalon1

from tests.first_functions import find_max_value
FIXTURE1 = [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 120, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook, yandex'),
    ({'facebook': 12, 'yandex': -120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'vk')
]
@pytest.mark.parametrize('stats, etalon', FIXTURE1)
def test_find_max_value(stats, etalon):
    result = find_max_value(stats)
    assert result==etalon

