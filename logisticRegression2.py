import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

def sigmoid(z):
    return 1/(1+np.exp(-z))

def predict(features,weights):
    z=np.dot(features,weights)
    a=sigmoid(z)
    return a

def costfunction(features,labels,weights):
    observations=len(labels)
    predictions=predict(features,weights)
    class1_cost=-labels*np.log(predictions)
    class2_cost=(1-labels)*np.log(1-predictions)
    cost=class1_cost-class2_cost
    cost=cost.sum()/observations
    return cost

def updateweights(features,labels,weights,learningrate):
    N=len(features)
    predictions=predict(features,weights)
    gradient=np.dot(features.T,predictions-labels)
    gradient/=N
    graient*=learningrate
    weights-=gradient
    return weights

def decisionboundary(probability):
    if probability>=0.5:
        return 1
    else:
        return 0

def classify(predictions):
    decisionboundary=np.vectorise(decisionboundary)
    return decisionboundary(predictions).flatten()

def train(features,labels,weights,learningrate,iterations):
    costhistory=[]
    for i in range(iterations):
        weights=updateweights(features,labels,weights,learningrate)
        cost=costfunction(features,labels,weights)
        costhistory.append(cost)
        
        if i%1000==0:
            print("Iteration: "+str(i)+" Cost: "+str(cost))  
    return weights,costhistory

def accuracy(predictedlabels,actuallabels):
    difference=predictedlabels-actuallabels
    return 1-float((np.count_nonzero(diff))/len(difference))

def plotdecisionboundary(trues,falses):
    fig=plt.figure()
    ax=fig.subplot(111)
    noofpredictions=len(trues)+len(falses)
    ax.scatter([i for i in range(len(trues))],trues,s=25,c='b',marker="o",label='Trues')
    ax.scatter([i for i in range(len(falses))],falses,s=25,c='r',marker="s",label='Falses')
    plt.legend(loc="upper right")
    ax.set_title("Decision boundary")
    ax.set_xlabel("N/2")
    ax.set_ylabel("Predicted Probability")
    plt.axhline(0.5,color="black")
    plt.show()

if __name__=="__main__":
    mycsvfile=pd.read_csv('./notebooks/glass.csv')
    X=mycsvfile[["RI","Na","Mg","Al","Si","K","Ca","Ba","Fe"]]
    Y=mycsvfile["Type"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=1)

    weights=np.zeros(len(X_train))
    predict(X_train,weights)
