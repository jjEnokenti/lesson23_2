from typing import Iterable, List

import utils

functions = {
    'filter': utils.my_filter,
    'map': utils.my_map,
    'limit': utils.my_limit,
    'sort': utils.my_sort,
    'unique': utils.my_unique,
    'regex': utils.regex,
}


def caller(cmd: str, value: str, data: Iterable) -> List[str]:
    return functions[cmd](value=value, data=data)  # type: ignore
