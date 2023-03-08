import json

from flask import Flask, request

from utils import mapper, is_exist, gen_file_data

app = Flask(__name__)


@app.route('/perform_query', methods=['POST'])
def perform_query():
    query = request.form
    try:
        file_name = query.get('file_name')

        cmd_1 = query.get('cmd1')
        value_1 = query.get('value1')

        cmd_2 = query.get('cmd2')
        value_2 = query.get('value2')
    except AttributeError:
        return '', 400

    if not is_exist(file_name=file_name):
        return '', 400

    data_from_file = gen_file_data(file_name)
    result = mapper(cmd_1, value_1, data_from_file)
    result = mapper(cmd_2, value_2, result)

    return json.dumps(list(result))


if __name__ == '__main__':
    app.run()
