import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

class LogitRegression():
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations
        
    def fit( self, X, Y ) :
        self.m, self.n = X.shape
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y
        for i in range(self.iterations):
            self.update_weights()
        return self

    def update_weights(self):
        A = 1 / (1 + np.exp(-(self.X.dot(self.W) + self.b)))
        tmp = (A - self.Y.T)
        tmp = np.reshape(tmp, self.m)
        dW = np.dot(self.X.T, tmp)/self.m
        db = np.sum(tmp)/self.m

        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db
        return self

    def predict( self, X ) :	
        Z = 1 / (1 + np.exp(-(X.dot(self.W) + self.b)))		
        Y = np.where( Z > 0.5, 1, 0 )		
        return Y

def main():
    df = pd.read_csv("./notebooks/diabetes.csv")
    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1:].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

    model = LogitRegression(learning_rate = 0.01, iterations = 1000)
    model.fit(X_train,Y_train)
    model1 = LogisticRegression()
    model1.fit( X_train, Y_train)
    Y_pred = model.predict(X_test)
    Y_pred1 = model1.predict(X_test)
    correctly_classified = 0
    correctly_classified1 = 0
    count = 0
    for count in range(np.size(Y_pred)):
        if Y_test[count] == Y_pred[count]:
            correctly_classified = correctly_classified + 1
        if Y_test[count] == Y_pred1[count]:
            correctly_classified1 = correctly_classified1 + 1
        count = count + 1

    print("Accuracy on test set by our model: ",(correctly_classified/count)*100)
    print("Accuracy on test set by sklearn model: ",(correctly_classified1/count)*100)


if __name__ == "__main__" :
    main()
