### Пример POST запроса
    {
        "file_name": "apache_logs.txt",
        "queries":
                [
                    {
                        "cmd": "regex",
                        "value": "images\/\\w+\\.png"
                    },
                    {
                        "cmd": "map",
                         "value": 0
                    },
                    {
                        "cmd": "limit",
                        "value": 3
                    },
                    ...
                ]
    }

### Результат
    [
        "193.238.231.119",
        "193.238.231.119",
        "193.238.231.119"
    ]
