from flask import Blueprint, request, make_response
from services

clustering = Blueprint("clustering", __name__)

@clustering.route("/nearest_neighbors", methods=["POST"])
def get_nearest_neighbors():
    data = request.get_json()
    #return SimpleRegressions.lineal(data)

@clustering.route("/logistics", methods=["POST"])
def get_logistics():
    data = request.get_json()
    #return SimpleRegressions.polynomial(data)