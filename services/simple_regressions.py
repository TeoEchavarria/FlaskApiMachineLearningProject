from flask import make_response

class SimpleRegressions:

    @classmethod
    def lineal():
        return make_response({"message" : "Lineal Simple Regression"})
    
    @classmethod
    def polynomial():
        return make_response({"message" : "Lineal Simple Regression"})