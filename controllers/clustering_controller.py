from flask import Blueprint, request, make_response
from services.clustering import Clustering

clustering = Blueprint("clustering", __name__)

@clustering.route("/nearest_neighbors", methods=["POST"])
def get_nearest_neighbors():
    data = request.get_json()
    return Clustering.nearestNeighbors(data)

@clustering.route("/logistics", methods=["POST"])
def get_logistics():
    data = request.get_json()
    return Clustering.logistics(data)