import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class PolynomialSimpleModel:

    @classmethod
    def prediction(self, dataset):
        X = np.array(dataset["X"]).reshape(-1, 1)
        y = np.array(dataset["Y"])

        regression = PolynomialFeatures(degree = 3)
        X_poly = regression.fit_transform(X)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_poly, y)

        X_grid = np.arange(min(X), max(X), 0.1)
        X_grid = X_grid.reshape(len(X_grid), 1)

        return {"error" : 0, "prediction" :  list(lin_reg_2.predict(regression.fit_transform(X_grid)))}

