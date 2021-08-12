from flask import Flask, jsonify, make_response
from flask_cors import CORS
from todo_repository import TodoRepository
from http_utils import HttpUtils

import os

global app 
global host
global port

app = None
host = None
port = None
cors = None

def init_app():
    global app 
    global host
    global port
    global cors

    if app is None:
        app = Flask(__name__)

    if cors is None:
        cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    if host is None:
        host = os.environ['API_PYTHON_HOST']

    if port is None:
        port = os.environ['API_PYTHON_PORT']

init_app()
repository = TodoRepository(app)
httputils = HttpUtils()
repository.create_all()

@app.route('/api/v1/todo', methods=['GET'])
def index():
    return make_response(jsonify({"todos": repository.get_all()}))

@app.route('/api/v1/todo/<id>', methods=['GET'])
def get_todo_by_id(id):
    return make_response(jsonify(repository.get(id)))

@app.route('/api/v1/todo/<id>', methods=['PUT'])
def update_todo_by_id(id):
    data = httputils.get_json_body()
    return make_response(jsonify(repository.update(id, data)))

@app.route('/api/v1/todo/<id>', methods=['DELETE'])
def delete_todo_by_id(id):
    repository.delete(id)
    return make_response("", 204)

@app.route('/api/v1/todo', methods=['POST'])
def create_todo():
    data = httputils.get_json_body()
    return make_response(jsonify(repository.insert(data)), 200)

if __name__ == "__main__":
    app.run(debug=False, host=host, port=port)
