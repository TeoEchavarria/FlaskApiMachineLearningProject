import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Lineal_Simpledeac_Model:

    @classmethod
    def prediction(dataset):
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

        regression = LinearRegression()
        regression.fit(X_train, y_train)

        y_pred = regression.predict(X_test)

        #EVALUACION DE % DE ERROR
        error_aprox = np.mean([ abs((y_pred[i]-y_test[i])/y_test[i]) for i in range(len(X_test))])

        return {"error" : error_aprox, "prediction" : [X_test, regression.predict(X_test)]}