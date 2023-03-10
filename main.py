from flask import Flask, request, jsonify
from marshmallow import ValidationError

from functions import caller
from models import RequestSchema
from my_exceptions import BadQuery
from utils import is_exist, gen_file_data

app = Flask(__name__)


@app.route('/perform_query', methods=['POST'])
def perform_query():  # type: ignore

    try:
        valid_data = RequestSchema().load(request.json)
    except ValidationError as error:
        return error, 400

    queries = valid_data.queries
    file_name = valid_data.file_name

    if not is_exist(file_name=file_name):
        return 'file not found', 404

    data = gen_file_data(file_name=file_name)
    result_data = []

    try:
        for cnt, query in enumerate(queries):
            cmd = query.cmd
            value = query.value
            if not cnt:
                result_data = caller(cmd, value, data)
            else:
                result_data = caller(cmd, value, data=result_data)
    except (AttributeError, BadQuery) as error:
        return error, 400
    else:
        return jsonify(result_data)


if __name__ == '__main__':
    app.run()
