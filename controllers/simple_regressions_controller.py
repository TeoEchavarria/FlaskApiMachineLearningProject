from flask import Blueprint, request, make_response
from services.simple_regressions import SimpleRegressions

simple_regressions_route = Blueprint("simple_regressions", __name__)

@simple_regressions_route.route("/lineal", methods=["GET"])
def get_lineal_simple_model():
    data = request.data
    return make_response(data)
    #return SimpleRegressions.lineal(data)

@simple_regressions_route.route("/polynomial", methods=["GET"])
def get_polynomial_simple_model():
    data = request.data
    return make_response(data)
    #return SimpleRegressions.polynomial(data)
