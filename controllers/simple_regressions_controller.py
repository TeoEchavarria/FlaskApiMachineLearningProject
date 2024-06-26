from flask import Blueprint, request, make_response
from services.simple_regressions import SimpleRegressions

simple_regressions_route = Blueprint("simple_regressions", __name__)

@simple_regressions_route.route("/lineal", methods=["POST"])
def get_lineal_simple_model():
    data = request.get_json()
    #return make_response({"message" : "lineal"})
    return SimpleRegressions.lineal(data)

@simple_regressions_route.route("/polynomial", methods=["POST"])
def get_polynomial_simple_model():
    data = request.get_json()
    #return make_response({"message" : "polynomial"})
    return SimpleRegressions.polynomial(data)
