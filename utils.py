import os
import re
from typing import List, Any

from settings import DATA_DIR


def my_filter(value: str, data: List[str]) -> List[str]:
    return list(filter(lambda line: value in line, data))


def my_map(value: int, data: List[str]) -> List[str]:
    value = int(value)
    return list(map(lambda line: line.split()[value], data))


def my_limit(value: int, data: List[str]) -> List[str]:
    value = int(value)
    return data[:value]


def my_unique(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def my_sort(value: str, data: List[str]) -> List[str]:
    value = value.lower()
    return sorted(data, reverse=False if value == 'asc' else True)


def regex(value: str, data: List[str]) -> List[str]:
    regexp = re.compile(value, re.IGNORECASE)
    return list(filter(lambda string: re.search(regexp, string), data))


def gen_file_data(file_name: str) -> List[str]:
    """Генератор строк данных из файла"""
    with open(os.path.join(DATA_DIR, file_name), encoding='utf-8') as file:
        return [line.strip() for line in file]
        # for line in file:
        #     yield line.strip()


def is_exist(file_name: str) -> bool:
    """Проверяет существует ли файл"""
    return os.path.exists(os.path.join(DATA_DIR, file_name))
