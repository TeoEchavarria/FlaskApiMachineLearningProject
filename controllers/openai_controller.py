from flask import Blueprint, request
from services.simple_regressions import SimpleRegressions

openai_route = Blueprint("openai_route", __name__)

@openai_route.route("/openai", methods=["GET"])
def get_lineal_simple_model():
    return SimpleRegressions.lineal()

@openai_route.route("/github", methods=["GET"])
def get_polynomial_simple_model():
    return SimpleRegressions.polynomial()
