from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.simple_regressions_controller import simple_regressions_route

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({"message" : 'Hello World Flask'})

app.register_blueprint(simple_regressions_route)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
