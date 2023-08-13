from flask import make_response
from models.NN import LinealSimpleModel
from models.logistic import PolynomialSimpleModel

class Clustering:

    @classmethod
    def nearestNeighbors(self, data):
        return make_response(LinealSimpleModel.prediction(data))
    
    @classmethod
    def logistics(self, data):
        return make_response(PolynomialSimpleModel.prediction(data))