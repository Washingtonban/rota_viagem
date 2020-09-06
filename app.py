import flask
from flask import jsonify, request

from model.route_search import RouteSearch
from model.data_connect import DataConnect



app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/update", methods=["POST"])
def update():
    model_update = DataConnect()
    json_response = request.get_json()
    if len(json_response['line']) == 3:
        model_update.updateCsv(data=json_response['data'], line=json_response['line'])
        return jsonify({"message": "New route successfully created"})
    else:
        return jsonify({"message": "New route fail created"})




@app.route("/api/route", methods=["POST"])
def route():
    json_response = request.get_json()
    model = RouteSearch(origem=json_response['origem'], destino=json_response['destino'])
    result = model.route_search()

    final = ''
    for item in result[1]:
        if item == result[1][-1]:
            final += f' {item}'
        else:
            final += f' {item} -'

    return f'{final} ao custo de ${result[0]}'


if __name__ == '__main__':
    app.run(debug=True)