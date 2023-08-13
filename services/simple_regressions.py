from flask import make_response
from models.simple.lineal import LinealSimpleModel
from models.simple.polynomial import PolynomialSimpleModel

class SimpleRegressions:

    @classmethod
    def lineal(self, data):
        return make_response(LinealSimpleModel.prediction(data))
    
    @classmethod
    def polynomial(self, data):
        return make_response(PolynomialSimpleModel.prediction(data))