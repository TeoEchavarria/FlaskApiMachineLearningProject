from flask import make_response
from models.lineal import LinealSimpleModel
from models.polynomial import PolynomialSimpleModel

class SimpleRegressions:

    @classmethod
    def lineal(self, data):
        return make_response(LinealSimpleModel.prediction(data))
    
    @classmethod
    def polynomial(self, data):
        return make_response(PolynomialSimpleModel.prediction(data))