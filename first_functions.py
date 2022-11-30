from pprint import pprint
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def find_russian_visits(log_list):
    new_list = []
    for el in log_list:
        if 'Россия' == list(el.values())[0][1]:
            new_list.append(el)
    return new_list

find_russian_visits(geo_logs)


def find_unique_values(ids):
    user1_set = set(ids["user1"])
    user2_set = set(ids["user2"])
    user3_set = set(ids["user3"])
    return user1_set|user2_set|user3_set
find_unique_values({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]})
def find_max_value(stats):
    values_list = list(stats.values())
    enumerated_keys = list(enumerate(stats))
    enumersted_values = list(enumerate(values_list))
    max_number = max(values_list)
    max_company = enumerated_keys[values_list.index(max_number)]
    return max_company[1]

find_max_value({'facebook': 120, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98})


