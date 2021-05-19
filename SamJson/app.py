from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def index():
    data = request.get_json(force=True)
    device = data["device"]
    result = {'deviceout': device}
    
    return jsonify(result)

@app.route('/samedia/add/origin', methods=['POST'])
def addOrigin():
    data = request.get_json(force=True)
    # gather origin inputs

    # generate origin data

    # return origin json
    out = {"ORIGIN": "OUTPUT ORIGIN"}
    return jsonify(out)

@app.route('/samedia/add/raw', methods=['POST'])
def addRaw():
    # gather raw inputs

    # generate raw data

    # return raw json
    out = {"RAW": "OUTPUT RAW"}
    return jsonify(out)

@app.route('/samedia/add/canon', methods=['POST'])
def addCanon():
    # gather canon inputs

    # generate canon data

    # return canon json
    out = {"CANON": "OUTPUT CANON"}
    return jsonify(out)

@app.route('/samedia/add/web', methods=['POST'])
def addWeb():
    # gather web inputs

    # gather web data

    # return web data
    out = {"WEB": "OUTPUT WEB"}
    return jsonify(out)

@app.route('/jsonfile/read', methods=['GET','POST'])
def readJsonFile():
    return "JSON"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')