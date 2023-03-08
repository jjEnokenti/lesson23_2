import os

from settings import DATA_DIR


def my_filter(value, data):
    return filter(lambda line: value in line, data)


def my_map(value, data):
    value = int(value)
    return map(lambda line: line.strip().split()[value], data)


def my_limit(value, data):
    value = int(value)
    return (line for ind, line in enumerate(data) if ind < value)


def my_unique(data, *args):
    return set(data)


def my_sort(value, data):
    value = value.lower()
    return sorted(data, reverse=False if value == 'asc' else True)


functions = {
    'filter': my_filter,
    'map': my_map,
    'limit': my_limit,
    'sort': my_sort,
    'unique': my_unique
}


def gen_file_data(file_name):
    """Генератор строк данных из файла"""
    with open(os.path.join(DATA_DIR, file_name), encoding='utf-8') as file:
        for line in file:
            line = line
            yield line


def is_exist(file_name):
    """Проверяет существует ли файл"""
    for _, _, files in os.walk(DATA_DIR):
        if file_name in files:
            return True
    return False
