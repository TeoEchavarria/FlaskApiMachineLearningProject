import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


class NearestNeighborsClusteringModel:

    @classmethod
    def prediction(self, dataset):
        X = np.array(list(filter(lambda x: x is not None, dataset["X"])))
        y = np.array(list(filter(lambda x: x is not None, dataset["Y"])))

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 0)


        # Escalado de variables
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)


        # Ajustar el modelo de Regresión Logística en el Conjunto de Entrenamiento
        classifier = KNeighborsClassifier(n_neighbors = 5, metric = "minkowski", p = 2)
        classifier.fit(X_train, y_train)

        # Predicción de los resultados con el Conjunto de Testing
        y_pred  = classifier.predict(X_test)

        # Elaborar una matriz de confusión
        cm = confusion_matrix(y_test, y_pred)
        return { "prediction" : [{"x" : i, "y" : j} for i,j in zip( X_test.tolist(), y_pred.tolist())] , "xTrain" : X_train.tolist()}