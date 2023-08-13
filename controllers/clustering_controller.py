from flask import Blueprint, request, make_response
from services.clustering import Clustering

clustering_route = Blueprint("clustering", __name__)

@clustering_route.route("/nearest_neighbors", methods=["POST"])
def get_nearest_neighbors():
    data = request.get_json()
    return Clustering.nearestNeighbors(data)

@clustering_route.route("/logistics", methods=["POST"])
def get_logistics():
    data = request.get_json()
    return Clustering.logistics(data)