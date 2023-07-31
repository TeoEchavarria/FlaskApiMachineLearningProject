from flask import Blueprint, request
from services.simple_regressions import SimpleRegressions

simple_regressions_route = Blueprint("simple_regressions", __name__)

@simple_regressions_route.route("/lineal", methods=["GET"])
def get_lineal_simple_model():
    data = request.get_json()
    print(data, type(data))
    return SimpleRegressions.lineal(data)

@simple_regressions_route.route("/polynomial", methods=["GET"])
def get_polynomial_simple_model():
    data = request.get_json()
    return SimpleRegressions.polynomial(data)
