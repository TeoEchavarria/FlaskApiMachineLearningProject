import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinealSimpleModel:

    @classmethod
    def prediction(self, dataset):
        X = np.array(list(filter(lambda x: x is not None, dataset["X"]))).reshape(-1, 1)
        y = np.array(list(filter(lambda x: x is not None, dataset["Y"])))

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 0)

        regression = LinearRegression()
        regression.fit(X_train, y_train)

        y_pred = regression.predict(X)

        #EVALUACION DE % DE ERROR
        error_aprox = np.mean([ abs((y_pred[i]-y_test[i])/y_test[i]) for i in range(len(X_test))])

        prediction =  list(y_pred)
        x_prediction = [i[0] for i in X.tolist()]

        return {"error" : 0, "prediction" : [{"x" : i, "y" : j} for i,j in zip(prediction, x_prediction)] , "xTrain" : x_prediction}