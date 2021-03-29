import numpy as np
import csv
myarr=np.genfromtxt('superfilteredFinal.csv',delimiter=',')
print(myarr)
print(myarr.shape)
print(myarr.T)
print("Ended one file")

mynewarr=np.genfromtxt('filteredFinal.csv',delimiter=',')
awesomestuff=mynewarr[:,1:]
print(awesomestuff)
print(awesomestuff.shape)
print(awesomestuff.T)

#my_data=pd.read_csv('superfilteredFinal.csv',sep=',',header=None)
#data_X=my_data.T
#print(data_X)
#print(data_X.shape)

#my_data=pd.read_csv('filteredFinal.csv',sep=',',header=None).T
#data_Y=my_data.iloc[1:,]
#print(data_Y)
#print(data_Y.shape)
