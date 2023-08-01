import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinealSimpleModel:

    @classmethod
    def prediction(self, dataset):
        X = np.array(dataset["X"]).reshape(-1, 1)
        y = np.array(dataset["Y"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

        regression = LinearRegression()
        regression.fit(X, y)

        y_pred = regression.predict(X)

        #EVALUACION DE % DE ERROR
        error_aprox = np.mean([ abs((y_pred[i]-y_test[i])/y_test[i]) for i in range(len(X_test))])

        return {"error" : error_aprox, "prediction" : list(regression.predict(X))}