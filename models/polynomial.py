import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class PolynomialSimpleModel:

    @classmethod
    def prediction(self, dataset):
        X = np.array(list(filter(lambda x: x is not None, dataset["X"]))).reshape(-1, 1)
        y = np.array(list(filter(lambda x: x is not None, dataset["Y"])))

        regression = PolynomialFeatures(degree = 5)
        X_poly = regression.fit_transform(X)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_poly, y)

        X_grid = np.arange(min(X), max(X), 0.1)
        X_grid = X_grid.reshape(len(X_grid), 1)

        prediction = list(lin_reg_2.predict(regression.fit_transform(X_grid)))
        x_prediction = [i[0] for i in X_grid.tolist()]

        return {"error" : 0, "prediction" : [{"x" : i, "y" : j} for i,j in zip(prediction, x_prediction)] }

