from flask import Flask, request, jsonify
from demo_flask.app.service import ToDoService, UserService
from demo_flask.app.models import Schema

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, " \
                                                       "X-Requested-With "
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return 'Hello World!'


@app.route("/<name>")
def hello_name(name):
    return 'Hello' + name


@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDoService().update(item_id, request.get_json()))


@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))


@app.route("/user", methods=["POST"])
def create_user():
    return jsonify(UserService().create(request.get_json()))


@app.route("/user", methods=["GET"])
def list_user():
    return jsonify(UserService().list())


if __name__ == '__main__':
    Schema()
    app.run(debug=True, host="0.0.0.0", port=8888)
