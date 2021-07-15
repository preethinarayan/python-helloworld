from flask import Flask
from flask import json
from flask.wrappers import Response
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successful!')
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK-Healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successful!')
    return response

@app.route("/metrics")
def metrics():
    data = {
            'UserCount': 140,
            'UserCountActive': 23
            }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successful!')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
