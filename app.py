import flask
from flask import jsonify, request

from model.data_connect import *


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/update", methods=["POST"])
def update():
    json_response = request.get_json()
    return jsonify(json_response)


@app.route("/api/route", methods=["POST"])
def route():
    json_response = request.get_json()
    return jsonify(json_response)


if __name__ == '__main__':
    app.run(debug=True)