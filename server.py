
from flask import Flask, request, jsonify
from simplex import Simplex, Result

app = Flask(__name__)

@app.route("/")
def home():
    return "Simplex Vettsel"

@app.route("/simplex", methods=['POST'])
def simplex():
    content = request.json

    table = []

    for i in content['data']:
        table.append(i)

    simplex = Simplex()
    stn = simplex.standardize(table)
    simplex_result = simplex.execute(stn)

    status = ""
    result = {}

    if (simplex_result['status'] == Result.infeasible):
        status = "impossivel"
    elif (simplex_result['status'] == Result.unbounded):
        status = "ilimitada"
    elif (simplex_result['status'] == Result.optimal):
        status = "otima"

        for row_item in simplex_result['table']:
            if (not isinstance(row_item[0], str)):
                result['x%s' % (str(row_item[0]))] = row_item[1]

        rows = len(simplex_result['table'][0]) - 2
        cols = len(simplex_result['table']) - 1
        for i in range((rows + cols) - 1):
            if (not ('x%s' % str(i + 1)) in result):
                result[('x%s' % str(i + 1))] = 0

    elif (simplex_result['status'] == Result.multi):
        status = "multiplas"

    return jsonify({ "data": { "status": status, "result": result } })

if __name__ == "__main__":
    app.run()
