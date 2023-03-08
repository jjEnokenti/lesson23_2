import os

from settings import DATA_DIR


def mapper(func_name, value, data):
    """Реализация функций передаваемых через запрос"""
    func_name = func_name.lower()

    if func_name == 'filter':
        return (line.split() for line in data if value in line)
    elif func_name == 'map':
        return (line[0].strip() for line in data)
    elif func_name == 'sort':
        value = value.lower()
        if value == 'asc':
            value = False
        elif value == 'desc':
            value = True
        return sorted(data, reverse=value)
    elif func_name == 'limit':
        return (line for ind, line in enumerate(data) if ind < value - 1)
    elif func_name == 'unique':
        return set(data)


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
