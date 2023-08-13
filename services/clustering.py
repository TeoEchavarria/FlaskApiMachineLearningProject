from flask import make_response
from models.clustering.logistics import LogisticClusteringModel
from models.clustering.nearestNeighbors import NearestNeighborsClusteringModel

class Clustering:

    @classmethod
    def nearestNeighbors(self, data):
        return make_response(NearestNeighborsClusteringModel.prediction(data))
    
    @classmethod
    def logistics(self, data):
        return make_response(LogisticClusteringModel.prediction(data))