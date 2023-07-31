import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class Lineal_Simpledeac_Model:

    @classmethod
    def prediction(dataset):
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

        regression = PolynomialFeatures(degree = 3)
        X_poly = regression.fit_transform(X)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_poly, y)

        X_grid = np.arange(min(X), max(X), 0.1)
        X_grid = X_grid.reshape(len(X_grid), 1)

        return {"error" : 0, "preddiction" : [X_grid, lin_reg_2.predict(regression.fit_transform(X_grid))]}

