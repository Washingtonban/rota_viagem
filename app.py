import flask
from flask import jsonify, request
from model.route_search import RouteSearch
from model.data_connect import DataConnect


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/update", methods=["POST"])
def update():
    model = DataConnect()
    json_response = request.get_json()
    result = model.updateCsv(data=json_response['data'], line=json_response['line'])
    return jsonify({"message": "New route successfully created"})



@app.route("/api/route", methods=["POST"])
def route():

    model = RouteSearch()
    json_response = request.get_json()
    result = model.route_search(origem=json_response['origem'], destino=json_response['destino'])

    final = ''
    for item in result[1]:
        if item == result[1][-1]:
            final += f' {item}'
        else:
            final += f' {item} -'

    return f'{final} ao custo de ${result[0]}'


if __name__ == '__main__':
    app.run(debug=True)