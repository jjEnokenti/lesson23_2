from dataclasses import dataclass
from typing import List, Union

import marshmallow_dataclass


@dataclass
class Query:
    cmd: str
    value: Union[str, int]


@dataclass
class Request:
    queries: List[Query]
    file_name: str


RequestSchema = marshmallow_dataclass.class_schema(Request)
